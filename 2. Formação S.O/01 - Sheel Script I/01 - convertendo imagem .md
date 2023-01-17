# Shell Script

É amplamente utilizado para automação de tarefas.

Os scripts são muito utilizados quando temos uma tarefa que precisa ser executada várias vezes, ao invés de digitarmos os comandos a cada vez, podemos consolidar em um script e executarmos esse script somente, proporcionando assim uma automatização de tarefas

**#!/bin/bash**: Essa primeira linha do script tem como finalidade indicar qual será o interpretador dos comandos presentes no script. Nesse caso, será utilizado o bash como sendo o interpretador

```mkdir scripts
cd scripts/
nano conversao-jpg-png.sh```

Criando o arquivo nano:

```#!/bin/bash
convert ~/Downloads/imagens-livros/algoritmos.jpj ~/Downloads/imagens-livros/algoritmos.png```

Salva esse arquivo.
Para rodar:

```
bash conversao-jpg-png.sh
```

Acessa a pasta e visualiza:
~cd/Download/imagens-livros

sabe-se que Para que seja possível pegar o conteúdo do primeiro parâmetro devemos referenciá-lo com o número 1 no nosso script, sendo precedido do símbolo $, ficando $1.

Logo: Altere o nome estático do livro algoritmos para pegar o conteúdo do primeiro parâmetro passado pelo usuário ($1);

```#!/bin/bash
convert ~/Downloads/imagens-livros/$1.jpj ~/Downloads/imagens-livros/$1.png```

 **$@**:O símbolo $@ é utilizado para referenciar todos os parâmetros passados por um usuário para nosso script, sem precisar ao certo quantos parâmetros são.

 Guarde o caminho **~/Downloads/imagens-livros** em uma constante, chamada por exemplo de **CAMINHO_IMAGENS**.

```
CAMINHO_IMAGENS = ~/Downloads/imagens-livros
for [variável] in $@
do
    convert $CAMINHO_IMAGENS/$[variável].jpg $CAMINHO_IMAGENS/$[variável].png
done 
```

Execute seu script passando como parâmetro os quatro próximos livros:

arduino_pratico
asp_net
big_data
codeigniter

No nosso script nós removemos o símbolo $@ e inserimos *.jpg.