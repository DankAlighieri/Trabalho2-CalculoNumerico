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

        const resultado = await chamarPython('trapezio', { a, b, n });

        if (resultado.erro) {
            exibirErro('resultado-integracao', resultado.erro);
            return;
        }

        let output = '✓ MÉTODO DO TRAPÉZIO\n\n';
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

        const resultado = await chamarPython('simpson', { a, b, n });

        if (resultado.erro) {
            exibirErro('resultado-integracao', resultado.erro);
            return;
        }

        let output = '✓ MÉTODO DE SIMPSON\n\n';
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
// INICIALIZAÇÃO
// ===================================

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    console.log('✓ Interface carregada com sucesso!');
});
