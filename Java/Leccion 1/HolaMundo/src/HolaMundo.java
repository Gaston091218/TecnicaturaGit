
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
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo); */
        
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
        
        
        
        
        
       
        
               
        
         
        
        
        
        
        
        
        
        
        
        
        

    }
                                   }
