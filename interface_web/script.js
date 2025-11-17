// ===================================
// GERENCIAMENTO DE ABAS
// ===================================

function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabId = button.getAttribute('data-tab');

            // Remover active de todos
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // Adicionar active ao clicado
            button.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
}

// ===================================
// LOADING OVERLAY
// ===================================

function showLoading() {
    document.getElementById('loading').classList.add('show');
}

function hideLoading() {
    document.getElementById('loading').classList.remove('show');
}

// ===================================
// UTILITÁRIOS
// ===================================

function parsearMatriz(texto) {
    const linhas = texto.trim().split('\n');
    const matriz = [];
    for (let linha of linhas) {
        if (linha.trim()) {
            const elementos = linha.split(',').map(x => parseFloat(x.trim()));
            matriz.push(elementos);
        }
    }
    return matriz;
}

function validarMatrizQuadradaEAvaliacao(A, b) {
    if (!Array.isArray(A) || A.length === 0) {
        throw new Error('Matriz A inválida');
    }
    const n = A.length;
    for (let i = 0; i < n; i++) {
        if (!Array.isArray(A[i]) || A[i].length !== n) {
            throw new Error('Matriz A deve ser quadrada (nxn)');
        }
    }
    if (!Array.isArray(b) || b.length !== n) {
        throw new Error('Vetor b deve ter o mesmo tamanho que A');
    }
}

function parsearVetor(texto) {
    return texto.split(',').map(x => parseFloat(x.trim()));
}

function exibirResultado(elementId, texto, tipo = 'success') {
    const elemento = document.getElementById(elementId);
    elemento.textContent = texto;
    elemento.className = `result-box ${tipo}`;
    elemento.classList.add('fade-in');
}

function exibirErro(elementId, mensagem) {
    exibirResultado(elementId, `❌ ERRO\n\n${mensagem}`, 'error');
}

// ===================================
// COMUNICAÇÃO COM BACKEND PYTHON
// ===================================

async function chamarPython(endpoint, dados) {
    try {
        showLoading();
        const response = await fetch(`http://localhost:5000/${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados)
        });

        if (!response.ok) {
            throw new Error('Erro na comunicação com o servidor');
        }

        const resultado = await response.json();
        hideLoading();
        return resultado;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

// ===================================
// MÉTODOS DIRETOS
// ===================================

async function executarGauss() {
    try {
        const matrizTexto = document.getElementById('matriz-a').value;
        const vetorTexto = document.getElementById('vetor-b').value;

        const A = parsearMatriz(matrizTexto);
        const b = parsearVetor(vetorTexto);

        // Validação cliente
        try {
            validarMatrizQuadradaEAvaliacao(A, b);
        } catch (e) {
            exibirErro('resultado-diretos', e.message);
            return;
        }

        const resultado = await chamarPython('gauss', { A, b });

        if (resultado.erro) {
            exibirErro('resultado-diretos', resultado.erro);
            return;
        }

        let output = '✓ ELIMINAÇÃO DE GAUSS\n\n';
        output += 'Solução:\n';
        resultado.x.forEach((valor, i) => {
            output += `  x[${i}] = ${valor.toFixed(8)}\n`;
        });

        exibirResultado('resultado-diretos', output);
    } catch (error) {
        exibirErro('resultado-diretos', error.message);
    }
}

async function executarLU() {
    try {
        const matrizTexto = document.getElementById('matriz-a').value;
        const vetorTexto = document.getElementById('vetor-b').value;

        const A = parsearMatriz(matrizTexto);
        const b = parsearVetor(vetorTexto);

        // Validação cliente
        try {
            validarMatrizQuadradaEAvaliacao(A, b);
        } catch (e) {
            exibirErro('resultado-diretos', e.message);
            return;
        }

        const resultado = await chamarPython('lu', { A, b });

        if (resultado.erro) {
            exibirErro('resultado-diretos', resultado.erro);
            return;
        }

        let output = '✓ FATORAÇÃO LU\n\n';
        
        output += 'Matriz L:\n';
        resultado.L.forEach(linha => {
            output += '  ' + linha.map(v => v.toFixed(6).padStart(12)).join('  ') + '\n';
        });
        
        output += '\nMatriz U:\n';
        resultado.U.forEach(linha => {
            output += '  ' + linha.map(v => v.toFixed(6).padStart(12)).join('  ') + '\n';
        });
        
        output += '\nSolução:\n';
        resultado.x.forEach((valor, i) => {
            output += `  x[${i}] = ${valor.toFixed(8)}\n`;
        });

        exibirResultado('resultado-diretos', output);
    } catch (error) {
        exibirErro('resultado-diretos', error.message);
    }
}

function limparDiretos() {
    document.getElementById('resultado-diretos').textContent = '';
    document.getElementById('resultado-diretos').className = 'result-box';
}

// ===================================
// MÉTODOS ITERATIVOS
// ===================================

async function executarGaussSeidel() {
    try {
        const matrizTexto = document.getElementById('matriz-iter').value;
        const vetorTexto = document.getElementById('vetor-iter').value;
        const tol = parseFloat(document.getElementById('tolerancia').value);
        const maxIter = parseInt(document.getElementById('max-iter').value);

        const A = parsearMatriz(matrizTexto);
        const b = parsearVetor(vetorTexto);

        // Validação básica
        try {
            validarMatrizQuadradaEAvaliacao(A, b);
        } catch (e) {
            exibirErro('resultado-iterativos', e.message);
            return;
        }

        const resultado = await chamarPython('gauss-seidel', { A, b, tol, maxIter });

        if (resultado.erro) {
            exibirErro('resultado-iterativos', resultado.erro);
            return;
        }

        let output = '✓ GAUSS-SEIDEL\n\n';
        output += `Iterações: ${resultado.iteracoes}\n`;
        output += `Tolerância: ${tol}\n\n`;
        output += 'Solução:\n';
        resultado.x.forEach((valor, i) => {
            output += `  x[${i}] = ${valor.toFixed(8)}\n`;
        });

        exibirResultado('resultado-iterativos', output);
    } catch (error) {
        exibirErro('resultado-iterativos', error.message);
    }
}

async function executarJacobi() {
    try {
        const matrizTexto = document.getElementById('matriz-iter').value;
        const vetorTexto = document.getElementById('vetor-iter').value;
        const tol = parseFloat(document.getElementById('tolerancia').value);
        const maxIter = parseInt(document.getElementById('max-iter').value);

        const A = parsearMatriz(matrizTexto);
        const b = parsearVetor(vetorTexto);

        // Validação básica
        try {
            validarMatrizQuadradaEAvaliacao(A, b);
        } catch (e) {
            exibirErro('resultado-iterativos', e.message);
            return;
        }

        const resultado = await chamarPython('jacobi', { A, b, tol, maxIter });

        if (resultado.erro) {
            exibirErro('resultado-iterativos', resultado.erro);
            return;
        }

        let output = '✓ JACOBI\n\n';
        output += `Iterações: ${resultado.iteracoes}\n`;
        output += `Tolerância: ${tol}\n\n`;
        output += 'Solução:\n';
        resultado.x.forEach((valor, i) => {
            output += `  x[${i}] = ${valor.toFixed(8)}\n`;
        });

        exibirResultado('resultado-iterativos', output);
    } catch (error) {
        exibirErro('resultado-iterativos', error.message);
    }
}

function limparIterativos() {
    document.getElementById('resultado-iterativos').textContent = '';
    document.getElementById('resultado-iterativos').className = 'result-box';
}

// ===================================
// INTERPOLAÇÃO
// ===================================

async function executarLagrange() {
    try {
        const xTexto = document.getElementById('pontos-x').value;
        const yTexto = document.getElementById('pontos-y').value;
        const xEval = parseFloat(document.getElementById('ponto-eval').value);

        const x = parsearVetor(xTexto);
        const y = parsearVetor(yTexto);

        const resultado = await chamarPython('lagrange', { x, y, xEval });

        if (resultado.erro) {
            exibirErro('resultado-interpolacao', resultado.erro);
            return;
        }

        let output = '✓ INTERPOLAÇÃO DE LAGRANGE\n\n';
        output += `Ponto avaliado: x = ${xEval}\n`;
        output += `Valor interpolado: y = ${resultado.yEval.toFixed(8)}`;

        exibirResultado('resultado-interpolacao', output);
    } catch (error) {
        exibirErro('resultado-interpolacao', error.message);
    }
}

async function executarMinimosQuadrados() {
    try {
        const xTexto = document.getElementById('pontos-x').value;
        const yTexto = document.getElementById('pontos-y').value;
        const xEval = parseFloat(document.getElementById('ponto-eval').value);

        const x = parsearVetor(xTexto);
        const y = parsearVetor(yTexto);

        const resultado = await chamarPython('minimos-quadrados', { x, y, xEval });

        if (resultado.erro) {
            exibirErro('resultado-interpolacao', resultado.erro);
            return;
        }

        let output = '✓ MÍNIMOS QUADRADOS\n\n';
        output += `Reta ajustada: y = ${resultado.a.toFixed(6)} + ${resultado.b.toFixed(6)}x\n\n`;
        output += `Ponto avaliado: x = ${xEval}\n`;
        output += `Valor: y = ${resultado.yEval.toFixed(8)}`;

        exibirResultado('resultado-interpolacao', output);
    } catch (error) {
        exibirErro('resultado-interpolacao', error.message);
    }
}

function limparInterpolacao() {
    document.getElementById('resultado-interpolacao').textContent = '';
    document.getElementById('resultado-interpolacao').className = 'result-box';
}

// ===================================
// INTEGRAÇÃO NUMÉRICA
// ===================================

async function executarTrapezio() {
    try {
        const a = parseFloat(document.getElementById('limite-a').value);
        const b = parseFloat(document.getElementById('limite-b').value);
        const n = parseInt(document.getElementById('num-intervalos').value);
        const func = document.getElementById('funcao-integracao')?.value || '';

        const resultado = await chamarPython('trapezio', { a, b, n, func });

        if (resultado.erro) {
            exibirErro('resultado-integracao', resultado.erro);
            return;
        }

        let output = '✓ MÉTODO DO TRAPÉZIO\n\n';
        output += `Função: ${resultado.funcao || 'x**2 (padrão)'}\n`;
        output += `Intervalo: [${a}, ${b}]\n`;
        output += `Número de intervalos: ${n}\n`;
        output += `Resultado: ${resultado.valor.toFixed(10)}`;

        exibirResultado('resultado-integracao', output);
    } catch (error) {
        exibirErro('resultado-integracao', error.message);
    }
}

async function executarSimpson() {
    try {
        const a = parseFloat(document.getElementById('limite-a').value);
        const b = parseFloat(document.getElementById('limite-b').value);
        const n = parseInt(document.getElementById('num-intervalos').value);
        const func = document.getElementById('funcao-integracao')?.value || '';

        // A implementação disponível no backend é Simpson 1/3 (n deve ser par)
        if (n % 2 !== 0) {
            exibirErro('resultado-integracao', 'Para Simpson 1/3, n deve ser um número par.');
            return;
        }

        const resultado = await chamarPython('simpson', { a, b, n, func });

        if (resultado.erro) {
            exibirErro('resultado-integracao', resultado.erro);
            return;
        }

        let output = '✓ MÉTODO DE SIMPSON 1/3\n\n';
        output += `Função: ${resultado.funcao || 'x**2 (padrão)'}\n`;
        output += `Intervalo: [${a}, ${b}]\n`;
        output += `Número de intervalos: ${n}\n`;
        output += `Resultado: ${resultado.valor.toFixed(10)}`;

        exibirResultado('resultado-integracao', output);
    } catch (error) {
        exibirErro('resultado-integracao', error.message);
    }
}

function limparIntegracao() {
    document.getElementById('resultado-integracao').textContent = '';
    document.getElementById('resultado-integracao').className = 'result-box';
}

// ===================================
// CARREGAR EXEMPLOS
// ===================================

function carregarExemploDiretos() {
    const sel = document.getElementById('exemplo-diretos');
    const val = sel.value;
    
    if (val === 'produtos') {
        // PROBLEMA 1: Produção de componentes eletrônicos
        // Sistema: 4T + 3R + 2C = 960 (cobre)
        //          1T + 3R + 1C = 510 (zinco)
        //          2T + 1R + 3C = 610 (vidro)
        document.getElementById('matriz-a').value = '4, 3, 2\n1, 3, 1\n2, 1, 3';
        document.getElementById('vetor-b').value = '960, 510, 610';
        exibirResultado('resultado-diretos', 'Exemplo carregado: Produção de componentes eletrônicos\n\nSistema:\n4T + 3R + 2C = 960 (cobre)\n1T + 3R + 1C = 510 (zinco)\n2T + 1R + 3C = 610 (vidro)\n\nClique em "Eliminação de Gauss" ou "Fatoração LU" para resolver.', 'success');
    }
}

function carregarExemploIterativos() {
    const sel = document.getElementById('exemplo-iterativos');
    const val = sel.value;
    
    if (val === 'circuito') {
        // PROBLEMA 3: Circuito elétrico com resistores
        document.getElementById('matriz-iter').value = '8.5, -2.5, 0, 0\n-2.5, 10.3, -3, 0\n0, -3, 12, -4\n0, 0, -4, 11';
        document.getElementById('vetor-iter').value = '16, 0, 0, 14';
        document.getElementById('tolerancia').value = '0.0001';
        document.getElementById('max-iter').value = '1000';
        exibirResultado('resultado-iterativos', 'Exemplo carregado: Circuito elétrico com resistores\n\nClique em "Gauss-Seidel" ou "Jacobi" para resolver.', 'success');
    }
}

function carregarExemploInterpolacao() {
    const sel = document.getElementById('exemplo-interpolacao');
    const val = sel.value;
    
    if (val === 'queda_tensao') {
        // PROBLEMA 2: Queda de voltagem em resistor
        document.getElementById('pontos-x').value = '0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 2.00';
        document.getElementById('pontos-y').value = '0.28, 0.67, 0.97, 1.42, 1.88, 6.0, 8.0';
        document.getElementById('ponto-eval').value = '0.85';
        exibirResultado('resultado-interpolacao', 'Exemplo carregado: Queda de voltagem em resistor\n\nPontos de corrente e voltagem carregados.\nPonto de avaliação: 0.85A\n\nClique em "Interpolação de Lagrange" para calcular.', 'success');
    }
}

function carregarExemploIntegracao() {
    const sel = document.getElementById('exemplo-integracao');
    const val = sel.value;
    
    if (val === 'area_rio') {
        // PROBLEMA 2: Área de um rio entre margens
        // Usa interpolação de Lagrange sobre os pontos, não função direta
        document.getElementById('limite-a').value = '0';
        document.getElementById('limite-b').value = '40';
        document.getElementById('num-intervalos').value = '4';
        document.getElementById('funcao-integracao').value = '';
        exibirResultado('resultado-integracao', 'Exemplo carregado: Área de um rio entre margens\n\n⚠️ NOTA: Este exemplo requer interpolação de pontos dados (M1, M2).\nPara implementar completamente, o backend precisa aceitar pontos x,y e criar interpolação.\n\nIntervalo: [0, 40], n=4\n\nPor enquanto, use uma função direta como x**2 para testar a integração.', 'success');
    }
}

// ===================================
// INICIALIZAÇÃO
// ===================================

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    console.log('✓ Interface carregada com sucesso!');
});
