# hate-speech-detection

Este projeto implementa modelos baseados em BERT e BERT-MLCNN para a detecção de discurso de ódio em português. O objetivo é comparar arquiteturas tradicionais de BERT com abordagens híbridas que combinam BERT com redes convolucionais (CNNs) de múltiplas camadas, avaliando o desempenho em datasets públicos como TuPyE e HATE-BR.

## Principais Modelos

- **BERTimbau**: Modelo BERT pré-treinado para português.
- **BERTabaporu**: Outro modelo BERT para português.
- **BERT-MLCNN**: Combinação de BERT (para extração de embeddings) com uma CNN multi-camadas para capturar padrões locais e hierárquicos no texto.

## Datasets

- **TuPyE**: Maior corpus público anotado para discurso de ódio em português, com múltiplas categorias (racismo, misoginia, lgbtfobia, etc.).
- **HATE-BR**: Corpus anotado para comentários em redes sociais.
- **UlyssesSD-Br**: Dataset para detecção de posicionamento (stance detection).

## Estrutura do Projeto

- `bert-mcnn.ipynb`: Notebook principal com experimentos, treinamento e avaliação dos modelos.
- `dataset.py`: Classe utilitária para carregamento e pré-processamento dos dados.
- `bertabaporu/` e `bertimbau/`: Pesos dos modelos treinados.
- `metrics/`: Métricas e históricos de treinamento.
- `article/`: Artigo científico descrevendo a metodologia e resultados.

## Como Executar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

2. Execute o notebook:
   - Abra `bert-mcnn.ipynb` no VSCode ou Jupyter.
   - Siga as células para treinar, avaliar e comparar os modelos.

## Resultados

Os experimentos mostram que a arquitetura BERT-MLCNN supera o BERT puro em tarefas multilabel e binárias, especialmente no dataset TuPyE, alcançando melhores métricas de precisão, recall e F1-score.

## Referências

- [BERTimbau](https://github.com/neuralmind-ai/portuguese-bert)
- [TuPyE Dataset](https://github.com/Silly-Machine/TuPyE-Dataset)
- [BERT-MLCNN Paper](https://www.sciencedirect.com/science/article/pii/S1319157823001325)

Veja detalhes completos de metodologia e resultados no artigo em [`article/article.tex`](article/article.tex).