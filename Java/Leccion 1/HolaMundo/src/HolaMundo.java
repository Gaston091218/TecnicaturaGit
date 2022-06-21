/*
import java.util.Scanner;

//Nuestro primer programa Hola Mundo
// Comentario
/*
Comentario extensivo de varias lineas
 */
public class HolaMundo {

    public static void main(String args[]) {//psvm + TAB
        /*
        System.out.println("Hola mundo desde Java"); //sout + TAB
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);

        //Tipo Sring
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
       
        //Var - Inferencia de tipos en Java
        var miVariavleEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 = " + miVariableCadena2); //soutv + tamb
        //atajo para ejecutar Shift + F6
        //Reglas para definir una variable en Java
        //No puede tener caracteres especiales ni empezar con mayuscula
        //Si puede iniciar con Guión bajo (_) y el signo dolar($)
        // Se puede usar acento pero NO es recomendable
        //No se puede usar el simbolo # para iniciar una variable
      
        var usuario = "Osvaldo";
        var titulo = " Ingeniero";
        var union = titulo +" "+ usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario (a + b));
         
        // Ejecucion de caracteres especiales con Java
        var nombre = "Maria";
        System.out.println("Nueva linea \n" + nombre);// salto de linea
        System.out.println("Tabulador:  \t" + nombre);// un espacio para centrar
        System.out.println("\t Menu");
        System.out.println("Retroceso: \b" + nombre);// Caracter de retroceso
        System.out.println("Comillas simples: \'" +nombre+"\'" );// Comillas simples
        System.out.println("Comillas dobles:\"" +nombre+"\""); //Comillas dobles
        
        // Clase Scanner
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite su nombre:");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo:");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " + titulo2+ " " +usuario2);
        
        byte numEnteroByte = (byte) 129;
        System.out.println("numEnteroByte = " + numEnteroByte); 
        System.out.println("Valor minimo del Byte:" + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte:" + Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del short:" + Short.MIN_VALUE);
        System.out.println("Valor maximo del short" + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del int"+ Integer.MAX_VALUE);
        
        long numEnteroLong = 10;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del long: "+ Long.MAX_VALUE);
        
        float numFloat = 3.40282335838F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del floar: " + Float.MIN_VALUE);
        System.out.println("Valor maximo del float:" + Float.MAX_VALUE);
        
        double numDouble = 1.9879879797987979788D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo del double:" + Double.MIN_VALUE);
        System.out.println("Valor maximo del double" + Double.MAX_EXPONENT);
        
        // Inferencia de tipos de var y tipo primitivos
        var numEntero =  20;// Las literales sin punto son de tipo entero
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F;// Automaticamente con el punto decimal se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        //Tipo Primitivos char
        char miVariable = 'a';
        System.out.println("miVariable = " + miVariable);
        char varCaracter = '\u2690';// Indicanmos a Java la asignación con el código unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 23; // Este es el valor decimaldel juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';// Un caracter especial, podemos copiar y pegar desde el unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo); 
        
        // Tipos de var
        var miVariable1 = 'a';
        System.out.println("miVariable1 = " + miVariable1);
        var varCaracter1 = '\u2690';// Indicanmos a Java la asignación con el código unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = 23; // Valor entero y ñe asomga un tipo int, si quiero que sea char pono (char) delante del numero
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$';// Un caracter especial, podemos copiar y pegar desde el unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'R';
        System.out.println("caracterChar = " + caracterChar);
        
        // tipos primitivos tipos booleanos
        boolean varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("la bandera es verde");
        }
        else{
            System.out.println("la bandera es roja");
        
        }
        // Algoritmo: ¿Es mayor de edad ?
        var edad = 10;// Literal Tener presente la inferencia de tipos
        // var adulto = edad >= 18; // Esta es una expresion
        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        // Conversion de tipos primitvos
         var edad = 20;
            System.out.println("edad =" + (edad + 1));
            var valorPi = Double.parseDouble ("3.1416");
            System.out.println("valorPi = " + valorPi);
         // Pedir un Valor
         var entrada = new Scanner (System.in);
         System.out.println("Digite su edad:");
         edad = Integer.parseInt(entrada.nextLine());
         System.out.println("edad = " + edad);
         //Covnersion de tipos primitivo en java parte 2
         var edadTexto = String.valueOf(10);
         System.out.println("edadTexto = " + edadTexto);
         
         var fraseChar = "Programadores".charAt(4);
         System.out.println("fraseChar = " + fraseChar);
         
         System.out.println("Digite un caracter: ");
         fraseChar = entrada.nextLine().charAt(0);
         System.out.println("fraseChar = " + fraseChar); 
         
        // Operadores aritmeticos
         int num1 = 5, num2 =  4;
         var solucion = num1 + num2;
         System.out.println("Solucion de la suma:" + solucion);
         
         solucion = num1  - num2;
         System.out.println("Solucion de la resta:" + solucion);
         
         solucion = num1  * num2;
         System.out.println("Solucion de la multiplicacion:" + solucion);
         
         solucion = num1  / num2;
         System.out.println("Solucion de la Division:" + solucion);
         
         var solucion2 = 3.4 / num2;
         System.out.println("solucion2 resultado de la divicion = " + solucion2);
         
         solucion = num1 % num2; // Guarda el residuo entero de la division
         System.out.println("solucion2 = " + solucion2);// 5/4
          if (num2 % 2 == 0)
              System.out.println("es un numero par");
          else
              System.out.println("el numero es impar");
          int varNum1 = 1, varNum2 = 4;
          int varNum3 = varNum1 + 6 - varNum2; // una operacion
          System.out.println("varNum3 = " + varNum3);
          
          varNum1 += 1; //varNum1 = varNum1 + 1; 
          System.out.println("varNum1 = " + varNum1);
          
          // -=  *=  /=  %=
          
          varNum1 -= 2;
          System.out.println("varNum2 = " + varNum2);
          
          varNum1 *= 5;
          System.out.println("varNum1 = " + varNum1);
                  
          varNum1 /= 4;
          System.out.println("varNum3 = " + varNum3);
          
          varNum1 %= 6;
          System.out.println("varNum1 = " + varNum1);
          
          // operadores unarios = cambio de signos
          var varA = 7;
          var varB = -varA;
          System.out.println("varA=" + varA);
          System.out.println("varB = " + varB); // la variable b sera de tipo negativo
          
          //operador de negacion
          var varC = true; //esta variable por defoult en java es de tipoboolean
          var varD = !varC;// aqui est invirtiendo el valor 
          System.out.println("varC = " + varC);
          System.out.println("varD = " + varD);
          
          //operadores unarios de incremento - preincremento
          var varE = 9;// se va a modificar su valor
          var varF = ++varE;// simbolo antes de la variable 
          //primero se incrementa la variable y despues se usa su valor
          System.out.println("varE = " + varE);//se incrementa en la unidad
          System.out.println("varF = " + varF);//va a sumar uno
          
          //postincremento (el simbolo va despues de la variable), luego el incremento
          var varG = 3;
          var varH = varG++;//primero el valor el valor de la variable luego el incremento
          System.out.println("varG = " + varG);
          System.out.println("varH = " + varH);
          
          //operadores de decremento
          var varI = 4;
          var varJ = --varI;//la variable ya esta en decremento
          System.out.println("varI = " + varI);
          System.out.println("varJ = " + varJ);
          
          //postdecremento
          var varK = 8;
          var varL = varK--;//primero el valor el valor de la variable luego el del decremento
          System.out.println("varK = " + varK);// aqui va el decremento en 1
          System.out.println("varL = " + varL);
        //operadores de igualdad y relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;//los parentesis son opcionales
        System.out.println("dNum = " + dNum);

        var cadenaA = "hola";
        var cadenaB = "adios";
        var cVar = cadenaA == cadenaB;//== no compara la variable de la cadena pero si sus referencias de objetos
        System.out.println("cVar = " + cVar);

        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);

        //operadores relacionales
        var gVar = aNum > bNum;//> < >= <= == !=(diferente)
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("el numero es par");
        } else {
            System.out.println("el numero es impar");

        }
        var edad = 15;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("es mayor de edad");
        } else {
            System.out.println("es menor de edad");
        }
        
        // operador condicional AND
         var valorA = 7;
         var valorMinimo = 0;//rango de 0 a 10
         var valorMaximo = 10;
         var respuesta = valorA >= 0 && valorA <= 10;//>= <= incluye el 0 y el 10
         // && (and) si una variable es verdadero el otro tambien es verdadero
         if (respuesta)
             System.out.println("esta dentro de rango");
         else
             System.out.println("esta fuera del rango");
         
        //operador OR
        var vacaciones = false;//or si uno es verdadero y el otro falso o viceversa da un verdadero
        var diaLibre = false;
        if (vacaciones || diaLibre)
            System.out.println("papa puede asistir");
        else 
            System.out.println("no puede aiatir");
        
        //operador ternario
        
        //segun la primera condicion te da un resultado y segun la segunda condicion da otro resultado
        var resultadoT = (5 > 8) ? "verdadero" : "falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0)? "Par" : "Impar";
        System.out.println("resultadoT = " + resultadoT);
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;//si x vale 5 va a pasar a valer 6 y si y vale 10 pasa a valer 9
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16
        
        var solucionAritmetica = 4 + 5 * 6 / 3; // 4 + (5 * 6) / 3 = 30 / 3 = 10 + 4 = 14
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3;//4 + 5 = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        */
        
    }
                                   
}