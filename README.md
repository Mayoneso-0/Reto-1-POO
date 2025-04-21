Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_1 en slack.

1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

P.D. El repositorio debe tener los archivos .py de los 5 puntos, uno por cada ejercicio. Asimismo una corta explicación de como llego a la solución.

1. Usando una funcion que cambie la operacion dependiendo del caracter que el usuario ingrese se hace esa operacion y se devuelve el resutlado
2. Con un bucle que compare el primer caracter de izquerda a derecha y el ultimo caracter, primero de derecha a izquierda, comparando si son iguales hasta que lleguen al mismo o hasta que no sean iguales
3. Seprar esa lista en enteros, con una funcion revisar que no tenga mas divisores que el 1 y el mismo para despues los que cumplan que son primos unirlos en una lista
4. Hacer la lista una lista de numeros enteros y con un bucle ir sumando primero con segundo, segundo con tercero, etc. Al tiempo guardar el mayor resultado y los numerons que son usados hasta que se acabe la lista
5. Convertir cada palabra en una lista de caractares, ordenar esa lista y comprar con otras palabras si es la misma o es diferente para que si es la misma se agregen a una lista final 
