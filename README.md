# Detectando rostos em vídeos
Com este código, você precisa apenas executá-lo e indicar o link do vídeo no YouTube.
Assim que isso for feito, o programa pedirá um nome para o arquivo.

Depois disso, todos os rostos que forem aparecendo serão detectados e enviados para uma pasta dentro do diretório do programa.

## Instação

Faça o download do código utilizando GIT ou utilize o ZIP disponível aqui no portal do GitHub.

*IMPORTANTE salientar que o código NÃO IDENTIFICA faces, apenas detecta-as em qualquer vídeo que for submetido ao algoritmo, podendo ser utilizado para outros fins como seleção de rosto de atores em filmes e novelas.

```sh
git clone https://github.com/cosmicpb/FascistFree.git

```

## Usando o script com o docker-compose


Passo 1 - Acesse o repositório do projeto:

```sh
cd FascistFree
```

Passo 2 - Gere o container:

```sh
docker-compose build
```

Passo 3 - Execute o container alterando o link para o seu link do YouTube:

```sh
LINK=https://www.youtube.com/watch?v=xxxx docker-compose run app
```

> Será gerada na pasta `dump` as imagens encontradas

> Nota: [Clique aqui](https://docs.docker.com/compose/install/) caso você não tenha o
docker-compose instalado.

## Usando o script
Passo 1 - Acesse o repositório do projeto:
```sh
cd FascistFree
```
Passo 2 - Instale as Libs (Bibliotecas) necessárias através do gerenciador de pacotes "pip":
```sh
pip install -r requirements.txt
```
Passo 3 - Execute o script Python:
```sh
python3 main.py
```
![alt text](https://uploaddeimagens.com.br/images/004/289/753/original/1.png?1673290162)
Serão criadas duas novas pastas:
1. video-opencv (com todos os frames capturados)
2. video-faces (com todas as faces detectadas nos frames capturados)

O código está capturando 1 frame por segundo. Para mudar esta taxa, modifique a seguinte linha de código:
```
SAVING_FRAMES_PER_SECOND = 1
```
Developed by Paulo


**FREE ASSANGE**

**Free Software, Hell Yeah!**
