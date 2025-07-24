
## Manejo de Memória 
AS linguagens de programação utilizam de objetos em seus programas para performar operações. Objetos incluem variáveis simples, do tipo strings, inteiros ou booleanos. E também incluem estruturas de dados mais complexas, como lists, hashes ou classes. 

O valo do objetos de seu programa é armazenado na memória para rápido acesso. N programação, uma variável é apenas um ponteiro para o endereço do objeto na memória. Quando uma variável é usada no programa, o código irá ler o valor que está sendo apontado e irá utiliza-lo. 

Na programação dos astecas, os desenvolvedores eram responsáveis pelo gerenciamento da memória em seus programas. Isso que dizer que, antes de criar uma lista ou objeto, primeiro era necessário alocar a memória para a variável.  E  depois de utilizar a variável, era necessário liberar a memória alocada anteriormente.
### E com isso surgiu dois problemas: 

1. Esquecer de liberar a memória: não liberar a memória alocada depois que ela não fosse mais necessária resultava em vazamento de memória (memory leaks). O que poderia resultar na utilização  desnecessária de memória. E para aplicações de longa duração, isso é um problema sério.
2. Liberando a memória muito cedo:  libertar a memória enquanto ela esta sendo utilizada pode resultar em um erro na aplicação, ou pode corromper os dados. Uma variável que aponta para uma memória que foi liberada é chamada de dangling pointer. 

Visando esses problemas e a impraticabilidade dessa prática, as novas linguagens adicionaram um gerenciamento de memória automático. 


## Gerenciamento de memória automático e Garbage Collection

Com gerenciamento de memória automático, os devs não precisam mais gerenciar a alocação da memória em suas aplicações, agora esse trabalho seria feito pelo runtime.

Tem algumas métodos de gerenciamento de memória automático. Os mais populares utilizam a contagem de referencias. Com a contagem de referencia, o runtime vigia todas as referencias a um objeto. Quando um objeto tem zero referencias, é inutilizável pelo programa e pode ser deletado.

Para os programadores, é uma mão na roda. Porém, essa automatização vem com um custo. 
Seu programa precisará utilizar mais memória e processamento para gerenciar essas referencias. E também, várias linguagens com gerenciamento automático de memória utilizam um processo "stop-the-world" para a colheita de objetos não utilizados, onde toda a execução é parada a fim de que o garbage collector procure e delete objetos a serem coletados. 

Mas como os computadores de hoje em dia  geralmente tem bastante memória RAM, esse lado negativo é superado facilmente.

Para aplicações de longa durabilidade onde a performance é essencial, algumas linguagens ainda tem presente o manejo de memória manual. Um exemplo  seria o C++. também está  presente em Objective-C, a linguagem utilizada para macOS e iOS. E para linguagens mais novas, o Rust também tem o manejo manual de memória.


## Como Python implementa o Garbage Collection
### *(Utilizando CPython)*

Existem dois tipos de gerenciamento de memória e garbage collection no CPython:
- Contagem de referencias
- Garbage Collection geracional

## Contagem de referencias no CPython
O principal mecanismo de coleta de lixo no CPython é a contagem de referências. Todo objeto Python tem um tipo (como lista ou função) e um contador de referências. Esse contador aumenta quando o objeto é referenciado e diminui quando deixa de ser. Se chegar a 0, o objeto é desalocado. Isso não pode ser desativado pelo seu código.

**✅ Resumo**:

- Cada objeto tem um contador de referências.
    
- Se não há mais referências, o objeto é destruído.
    
- A contagem não pode ser desativada.

### 🔍 **Visualizando a Contagem de Referências**
Você pode usar o módulo `sys` para ver a contagem de referências. Ela aumenta quando:

1. Atribui-se o objeto a uma variável
    
2. O objeto é colocado em uma estrutura (lista, dicionário etc.)
    
3. O objeto é passado como argumento
    

Exemplo:

```python
import sys
a = 'my-string'
sys.getrefcount(a)  # Resultado: 2

```

**✅ Resumo**:

- Use `sys.getrefcount(obj)` para ver o número de referências.
    
- Adicionar o objeto a estruturas ou passá-lo a funções aumenta a contagem.


### 🔄 **Problema: Ciclos de Referência**

Se um objeto faz referência a si mesmo (ex: um atributo apontando para o próprio objeto), mesmo que você o delete, ele continua na memória. Isso ocorre porque a contagem de referência nunca chega a 0.

**✅ Resumo**:

- Ciclos de referência (ex: `obj.a = obj`) **não são detectados** pela contagem.
    
- É aí que entra o **coletor de lixo generacional**.
    

---

### 🧬 **Coletor de Lixo Generacional – Conceitos**

- **Geração**: Objetos novos estão na geração 0. Se sobreviverem à coleta, vão para a geração 1, depois 2.
    
- **Limite (Threshold)**: Cada geração tem um número limite de objetos. Ao ultrapassar, o coletor é acionado.
    

**✅ Resumo**:

- O coletor divide objetos em **3 gerações**.
    
- Quanto mais "velho" o objeto, menos frequentemente ele será verificado.
    

---

### 👨‍💻 **Como isso afeta você como desenvolvedor**

Na prática, não se preocupe com o coletor de lixo na maioria dos casos. Python cuida disso para você. Alterar o comportamento dele raramente vale a pena. Se tiver problema de desempenho, normalmente é melhor melhorar a infraestrutura do que mexer nisso.

**✅ Resumo**:

- **Regra geral:** não altere o comportamento do coletor de lixo.
    
- É melhor investir em **infraestrutura mais forte** se houver problemas de desempenho.


Fonte: https://stackify.com/python-garbage-collection/
