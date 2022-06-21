package Leccion2;

import java.util.Scanner;


public class Leccion2 {

    public static void main(String[] args) {
/*
        var condicion = false;
        if (condicion) {
            System.out.println("Condicion Verdadera");//Codicional simple
        } else {
            System.out.println("Condicion Falsa");// Condicional doble
        }
        // Ejercicio estructura if else

        var numero = 2;
        var numeroTexto = "Numero Desconocido";
        if (numero == 1) {
            numeroTexto = " Numero uno";
        }
        if (numero == 2) {
            numeroTexto = "Numero dos";
        } else if (numero == 3) {
            numeroTexto = "Numero 3";
        } else if (numero == 4) {
            numeroTexto = "Numero 4";
        } else {
            numeroTexto = "Numero no encontrado";
        }
         System.out.println("numeroTexto = " + numeroTexto);
        } */
    Scanner entrada = new Scanner (System.in);
        System.out.println("Digite un numero del 1 al 4 :");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto =" Valor desconocido";
        switch (numero){
            case 1:
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4 :
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "Caso No encontrado";
        }
                System.out.println("numeroTexto = " + numeroTexto);
                
                
                
        }
        
    
    
    
  
        
    }


