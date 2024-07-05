// Espera o DOM estar completamente carregado antes de inicializar os tooltips
document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

document.getElementById('confirmSendButton').addEventListener('click', function () {
        enviarVenda();
    });


});

/**
 * Calcula os totais e atualiza os campos com os valores calculados.
 */
function calcular() {
    document.getElementById("msgModificaçãoDesconto").style = "display:none;";
    const listaItens = JSON.parse(localStorage.getItem("listaItens") || "[]");

    const { totalPreco, totalDescontoBruto, quantidadeProduto } = calcularTotais(listaItens);
    atualizarCamposTotais(totalPreco, totalDescontoBruto, quantidadeProduto);
    handleDescontoTotalChange(listaItens, totalPreco);
}

/**
 * Calcula os totais de preço, desconto bruto e quantidade de produtos.
 * @param {Array} listaItens - Lista de itens de venda.
 * @returns {Object} - Objeto contendo os totais de preço, desconto bruto e quantidade de produtos.
 */
function calcularTotais(listaItens) {
    let totalPreco = 0;
    let totalDescontoBruto = 0;
    let quantidadeProduto = 0;

    listaItens.forEach(itemVenda => {
        totalPreco += calcularTotalVenda(itemVenda);
        totalDescontoBruto += calcularTotalDesconto(itemVenda);
        quantidadeProduto += itemVenda.quantidade;
    });

    return { totalPreco, totalDescontoBruto, quantidadeProduto };
}

/**
 * Atualiza os campos de totais na interface.
 * @param {number} totalPreco - Total do preço dos itens.
 * @param {number} totalDescontoBruto - Total do desconto bruto dos itens.
 * @param {number} quantidadeProduto - Quantidade total de produtos.
 */
function atualizarCamposTotais(totalPreco, totalDescontoBruto, quantidadeProduto) {
    document.getElementById("totalVendaInput").value = (totalPreco - totalDescontoBruto).toFixed(2);
    const descontoMedioPercentual = Math.abs((((totalPreco - totalDescontoBruto) / totalPreco) * 100) - 100);
    document.getElementById("descontoInput").value = `${descontoMedioPercentual.toFixed(2)}%`;
    document.getElementById("comissaoInput").value = "3%";
}

/**
 * Lida com a mudança no total de desconto e aplica descontos proporcionais aos itens.
 * @param {Array} listaItens - Lista de itens de venda.
 * @param {number} totalPreco - Total do preço dos itens.
 */
function handleDescontoTotalChange(listaItens, totalPreco) {
    const descontoTotalInput = document.getElementById("descontoInput");

    descontoTotalInput.addEventListener("change", function () {
        const descontoTotalPercentual = parseFloat(descontoTotalInput.value) || 0;
        const totalVendaComDesconto = totalPreco - (totalPreco * (descontoTotalPercentual / 100));
        const descontoTotalBruto = totalPreco * (descontoTotalPercentual / 100);

        listaItens.forEach(itemVenda => {
            aplicarDescontoProporcional(itemVenda, totalPreco, descontoTotalBruto);
        });

        document.getElementById("totalVendaInput").value = totalVendaComDesconto.toFixed(2);
        document.getElementById("msgModificaçãoDesconto").style = "display:show;";
    });
}

/**
 * Aplica o desconto proporcional a um item de venda.
 * @param {Object} itemVenda - Objeto contendo informações do item de venda.
 * @param {number} totalPreco - Total do preço dos itens.
 * @param {number} descontoTotalBruto - Total do desconto bruto dos itens.
 */
function aplicarDescontoProporcional(itemVenda, totalPreco, descontoTotalBruto) {
    const precoProduto = Number(document.getElementById(`preco${itemVenda.produtoId}Input`).value) || 0;
    const descontoProporcional = (totalPreco > 0) ? (precoProduto * itemVenda.quantidade / totalPreco) : 0;
    const descontoItem = (descontoProporcional * (descontoTotalBruto));

    itemVenda.desconto = Number(descontoItem).toFixed(2);
    calcularTotal(itemVenda);

    document.getElementById(`desconto${itemVenda.produtoId}Input`).value = descontoItem.toFixed(2);
    alterarItemlistaItens(itemVenda);

    const descontoTotalInput = document.getElementById("descontoInput");
    const descontoTotalPercentual = parseFloat(descontoTotalInput.value) || 0;
    descontoTotalInput.value = `${descontoTotalPercentual.toFixed(2)}%`;
}

/**
 * Calcula o total de venda de um item.
 * @param {Object} itemVenda - Objeto contendo informações do item de venda.
 * @returns {number} - Total de venda do item.
 */
function calcularTotalVenda(itemVenda) {
    const precoProduto = Number(document.getElementById(`preco${itemVenda.produtoId}Input`).value) || 0;
    return precoProduto * itemVenda.quantidade;
}

/**
 * Calcula o total de desconto de um item.
 * @param {Object} itemVenda - Objeto contendo informações do item de venda.
 * @returns {number} - Total de desconto do item.
 */
function calcularTotalDesconto(itemVenda) {
    return Number(itemVenda.desconto);
}

/**
 * Limpa todos os dados de venda do localStorage.
 */
function limparVenda() {
    localStorage.clear();
}

/**
 * Obtém a data atual formatada como YYYY-MM-DD.
 * @returns {string} - Data atual formatada.
 */
function obterDataAtual() {
    const dataAtual = new Date();
    const ano = dataAtual.getFullYear();
    const mes = ('0' + (dataAtual.getMonth() + 1)).slice(-2);
    const dia = ('0' + dataAtual.getDate()).slice(-2);
    return `${ano}-${mes}-${dia}`;
}

/**
 * Formata a lista de itens, alterando a chave 'produtoId' para 'produto'.
 * @param {Array} listaItens - Lista de itens de venda.
 * @returns {Array} - Lista de itens formatada.
 */
function formatarProdutoId(listaItens) {
    listaItens.forEach(item => {
        if ('produtoId' in item) {
            item.produto = item.produtoId;
            delete item.produtoId;
        }
    });
    return listaItens;
}

/**
 * Envia a venda para o servidor.
 */
async function enviarVenda() {
    const cliente = localStorage.getItem("clienteId");
    const vendedor = localStorage.getItem("vendedorId");
    const listaItens = localStorage.getItem('listaItens');

    if (!cliente || !vendedor || !listaItens) {
        document.getElementById("msgErroCampo").style = "display: show;";
        document.getElementById("closeModalSend").click()
    }
    

    const dataHora = obterDataAtual();
    const tipoPagamento = document.getElementById("parcelasSelect").value;

    const venda = {
        vendedor: vendedor,
        cliente: cliente,
        data_venda: dataHora,
        tipo_pgto: tipoPagamento > 1 ? 2 : 1,
        parcelas_pgto: tipoPagamento > 1 ? tipoPagamento - 1 : 0,
        itens: formatarProdutoId(JSON.parse(listaItens))
    };

    try {
        const response = await fetch('/api/vendas/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(venda)
        });

        const contentType = response.headers.get('content-type');
        if (response.ok) {
            if (contentType && contentType.indexOf('application/json') !== -1) {
                const data = await response.json();
                console.log('Venda criada com sucesso:', data);
            } else {
                console.log('Resposta não é JSON:', await response.text());
            }
        } else {
            if (contentType && contentType.indexOf('application/json') !== -1) {
                const errorData = await response.json();
                console.error('Erro ao criar venda:', errorData);
            } else {
                console.error('Erro ao criar venda. Resposta não é JSON:', await response.text());
            }
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
    }
    localStorage.clear();
    location.reload();
}
