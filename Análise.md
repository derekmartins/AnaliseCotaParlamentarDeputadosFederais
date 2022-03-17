# O que é a Cota Parlamentar?

A seguir, são expostas as explicações pertinentes a cada elemento de dado publicado como "Dados Abertos" acerca das despesas realizadas e publicadas na Transparência, quanto ao uso da CEAP (Cota para o Exercício da Atividade Parlamentar). Essas despesas se confirmam por meio de lançamento de débitos contra a cota do deputado e podem decorrer em razão de uma das causas a seguir: pelo reembolso de documentos fiscais emitidos (Notas Fiscais, Recibos ou Despesa no Exterior); ou pelo custeio de despesas telefônicas; ou pelo débito de requisição de serviços postais; ou pela emissão de bilhetes aéreos.


# Quais despesas a Cota Parlamentar cobre?

Segundo a [ATO DA MESA N. 43, de 21/05/2009](http://imagem.camara.gov.br/Imagem/d/pdf/DCD22MAI2009sup.pdf#page=3), 
a Cota Parlamentar cobre custos de passagens aéreas, serviços postais, 
manutenção de escritórios de apoio à atividade parlamentar como locação 
de imóveis, IPTU, energia, água e esgoto, equipamentos, licenças de software, 
alimentação, hospedagem (exceto para parlamentares no DF), combustíveis 
(Até 4500), Segurança (Até 4500), Consultorias, Pesquisas Socioeconômicas.


# Alguns Fatos Interessantes Para Pesquisar

1. O único tipo de serviço que a nota pode ser no CPF é Aluguel de casa.
Artigo 4, Parágrafo 8, é dado da seguinte forma:
> É vedado o reembolso do pagamento realizado a pessoa física, salvo na
hipótese de locação de imóvel previsto na alínea "a" do Inciso III do Artigo 4
e no caso de local ou fretamento de aeronave e embarcação.

2. O deputado tem 90 dias após a compra para apresentar a documentação comprobatória.
(Artigo 4 Parágrafo 12)

3. A cota não pode ser usada para ressarcir despesas relativas a bens ou produtos
fornecidos por empresa ou entidade da qual o proprietário ou detentor de qualquer
participação seja Deputado ou Parente de até 3° grau. (Artigo 4 Parágrafo 13)

4. As demais despesas só podem ser cobertas mediante a aprovação do Presidente da
Câmara do Deputados. (§ 15 do Artigo 4)

1. E se o valor dos gastos exceder a Cota Parlamentar, o que ocorre?
O valor que excede é descontado automaticamente e integralmente do salário do 
Deputado. (§ 2 do Artigo 13)


# Dicionários dos Dados

> **txNomeParlamentar** - Nome adotado pelo Parlamentar ao tomar posse do seu mandato

> **cpf** - em caso de partidos políticos está ausente

> **ideCadastro** - Número que identifica unicamente um deputado federal na CD

> **nuCarteiraParlamentar** - Documento usado para identificar um deputado federal na CD. Pode alterar a cada Legislatura nova.

> **nuLegislatura** - número da legislatura

> **sgUF** - No contexto da cota CEAP, representa a unidade da federação pela qual o deputado foi eleito e é utilizada para definir o valor da cota a que o deputado tem

> **sgPartido** - sigla do Partido do parlamentar

> **codLegislatura** - código da legislatura

> **numSubCota** - Número da Subcota. Representa o código do Tipo de Despesa referente à despesa realizada pelo deputado e comprovada por meio da emissão de um documento fiscal, a qual é debitada na cota do deputado.

> **txtDescricao** - O seu conteúdo é a descrição do Tipo de Despesa relativo à despesa em questão

> **numEspecificacaoSubCota** - Número da Especificação da Subcota. Há despesas cujo Tipo de Despesa necessita ter uma especificação mais detalhada (por exemplo, “Combustível”). O conteúdo deste dado representa o código desta especificação mais detalhada.

> **txtDescricaoEspecificacao** - Descrição da Especificação da Subcota. Representa a descrição  especificação mais detalhada de um referido Tipo de Despesa.

> **txtFornecedor** - nome do fornecedor do produto ou serviço presente no documento fiscal

> **txtCNPJCPF** - O conteúdo deste dado representa o CNPJ ou o CPF do emitente do documento fiscal, quando se tratar do uso da cota em razão do reembolso despesas comprovadas pela emissão de documentos fiscais

> **txtNumero** - Número do documento. O conteúdo deste dado representa o número de face do documento fiscal emitido ou o número do documento que deu causa à despesa debitada na cota do deputado.

> **indTipoDocumento** - Este dado representa o tipo de documento do fiscal – 0 (Zero), para Nota Fiscal; 1 (um), para Recibo; e 2, para Despesa no Exterior.

> **datEmissao** - O conteúdo deste dado é a data de emissão do documento fiscal ou a data do documento que tenha dado causa à despesa

> **vlrDocumento** - valor do documento emitido. Quando se tratar de bilhete aéreo, esse valor poderá ser negativo, significando que o referido bilhete é um bilhete de compensação, pois compensa um outro bilhete emitido e não utilizado pelo deputado (idem para o dado vlrLiquido abaixo)

> **vlrGlosa** -  representa o valor da glosa do documento fiscal que incidirá sobre o Valor do Documento, ou o valor da glosa do documento que deu causa à despesa

> **vlrLiquido** - O seu conteúdo representa o valor líquido do documento fiscal ou do documento que deu causa à despesa e será calculado pela diferença entre o Valor do Documento e o Valor da Glosa. É este valor que será debitado da cota do deputado. Caso o débito seja do Tipo Telefonia e o valor seja igual a zero, significa que a despesa foi franqueada

> **numMes** - Mês da competência financeira do documento fiscal ou do documento que deu causa à despesa

> **numAno** -  Ano da competência financeira do documento fiscal ou do documento que deu causa à despesa

> **numParcela** - representa o número da parcela do documento fiscal. Ocorre quando o documento tem de ser reembolsado de forma parcelada

> **txtPassageiro** - nome do passageiro, quando o documento que deu causa à despesa se tratar de emissão de bilhete aéreo

> **txtTrecho** - trecho da viagem, quando o documento que deu causa à despesa se tratar de emissão de bilhete aéreo.

> **numLote** - número do lote. Representa uma capa de lote que agrupa os documentos que serão entregues à Câmara para serem ressarcidos. Este dado, juntamente com o Número do Ressarcimento, auxilia a localização do documento no Arquivo da Casa.

> **numRessarcimento** -  indica o ressarcimento do qual o documento fez parte por ocasião do processamento do seu reembolso. 

> **vlrRestituicao** -  representa o valor restituído do documento fiscal que incidirá sobre o Valor do Documento.

> **nuDeputadoId** - Número que identifica um Parlamentar ou Liderança na Transparência da Cota para Exercício da Atividade Parlamentar.

> **ideDocumento** - id do documento  

> **urlDocumento** - URL de acesso ao documento emitido


# Despesas que podem ser pagas com a Cota Parlamentar

As despesas que podem ser pagas com os recursos da Cota Parlamentar são: 

1. passagens aéreas;
2. telefones dos gabinetes, dos escritórios nos estados e dos imóveis funcionais, e as despesas com o celular funcional do deputado. As contas devem ser de comprovada responsabilidade do parlamentar;
3. serviços postais, exceto selos;
4. manutenção de escritórios de apoio à atividade parlamentar, como locação de imóveis, energia elétrica, água e esgoto, acesso à internet, entre outros;
5. alimentação do deputado;
6. hospedagem, exceto no Distrito Federal;
7. despesas com locomoção por:
> locação ou fretamento de aeronaves;
> locação ou fretamento de veículos automotores (limite inacumulável de R$ 12.713,00 mensais), permitida contratação de seguro;
> locação ou fretamento de embarcações;
> serviços de táxi, pedágio e estacionamento (limite inacumulável de R$ 2.700,00 mensais);
> passagens terrestres, marítimas ou fluviais.
8. combustíveis e lubrificantes (limite inacumulável de R$ 6.000,00 mensais);
9. serviços de segurança de empresas especializadas (limite inacumulável de R$ 8.700,00 mensais);
10. consultorias e trabalhos técnicos de apoio ao exercício parlamentar;
11. divulgação da atividade parlamentar (exceto nos 120 dias anteriores à data das eleições, se o deputado for candidato - Ato da Mesa 40/2012);
12. participação em cursos, congressos ou eventos, realizados por instituição especializada (limite mensal inacumulável de 25% do valor da menor cota – hoje R$7.697,17);
13. complementação de auxílio-moradia, de acordo com o Ato da Mesa 104/88 (limite inacumulável de R$1.747,00 mensais). 


# Despesas que não podem ser pagas com a Cota Parlamentar 

1. bens ou serviços adquiridos de empresa ou entidade da qual o deputado ou parente até o terceiro grau ou servidor da Câmara seja proprietário ou detentor de qualquer participação;
2. locação ou fretamento em empresas em que o deputado ou parente até o terceiro grau ou em que um servidor da Câmara sejam proprietários ou detentores de qualquer participação;
3. pagamento realizado à pessoa física, salvo para locação de imóvel, uso de aeronave ou embarcação, e serviços de táxi;
4. sem apresentação de nota fiscal, salvo se a empresa estiver legalmente isenta de emitir a nota;
5. aquisição de gêneros alimentícios;
6. aquisição de material permanente, de duração superior a dois anos;
7. locação de bens móveis com cláusulas que possibilitem sua aquisição com recursos da Cota;
8. locação de veículo automotor, prestada por pessoa jurídica especializada, que contemple o serviço de motorista;
9. gastos de caráter eleitoral;
10. gastos referentes à participação do deputado em cursos de educação básica, graduação e pós-graduação. 

Nos 120 dias anteriores à data das eleições gerais e municipais, os deputados que forem candidatos não poderão utilizar recursos da cota para pagar divulgação da atividade parlamentar (Ato da Mesa 40/2012).


# Informações sobre dados nulos

> A coluna vlrRestituicao possui 99% dos seus valores faltantes.
> A coluna txtDescricaoEspecificacao possui 77% dos seus valores faltantes.
> A coluna txtTrecho possui 70% dos seus valores faltantes.
> A coluna txtPassageiro possui 70% dos seus valores faltantes.
> A coluna numRessarcimento possui 61% dos seus valores faltantes.
> A coluna urlDocumento possui 41% dos seus valores faltantes.

As demais colunas com dados faltantes são praticamente irrisórias no universo amostral

# Valores negativos nas colunas vlrDocumento e vlrLíquido

Usando o método describe() conseguimos visualizar valores negativos nas colunas citadas. Buscando mais informações, descobrimos no dicionário que quando se tratar de bilhete aéreo, esse valor poderá ser **negativo**, significando que o referido bilhete é um bilhete de compensação, pois compensa um outro bilhete emitido e não utilizado pelo deputado (idem para o dado vlrLiquido abaixo).

