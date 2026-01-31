# `lflatten`
Achate e reconstrua estrutura de dados simples ou complexas.

## Tipos
- [Flatten](#type-flatten)

## Métodos
- [flatten](#flatten-flattenany-data-str-sep--str-prefix-bool-ignore_none)
- [unflatten](#dict-unflattenflatten-data-str-sep)
---

### `type Flatten`
Estrutura de dados onde as chaves são `strings` e os valores são `valores primitivos`

> Exemplos:
```py
{
    "foo.bar": 10
}
```
```py
{
    "person.name": "Jonas",
    "person.age": 16
}
```
```py
{
    "message.0.author": "Jonas",
    "message.0.value": "Hello, World!",
    "message.1.author": "Ana",
    "message.1.value": "Hii ^-^"
}
```
---

### `Flatten flatten(any data, str? sep, *, str? prefix, bool? ignore_none)`
Achata uma estrutura de dados:
```py
data = {
    "foo": {
        "bar": "Hello!"
    }
}
fdata = flatten(data)
print(fdata)
# saída:
{"foo.bar": "Hello!"}
```
| Tipo | Nome | Descrição | Padrão |
| - | - | - | :-: |
| `any` | `data` | Informação a ser achatada |
| `str?` | `sep` | Separador entre as chaves |
| `str?` | `prefix` | Prefixo das chaves | `.` |
| `bool?` | `ignore_none` | Ignorar valores `None` | `True` |

---

### `dict unflatten(Flatten data, str? sep)`
Reconstroi uma estrutura achatada.

```py
fdata = {"foo.bar": "Hello!"}
data = unflatten(data)
print(data)
# saída:
{
    "foo": {
        "bar": "Hello!"
    }
}
```
| Tipo | Nome | Descrição | Padrão |
| - | - | - | :-: |
| `Flatten` | `data` | Informação a ser reconstruída |
| `str?` | `sep` | Separador entre as chaves | `.` |