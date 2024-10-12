import java.util.Scanner;

public class ex3_30_08 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int[] numbers = new int[6];
        int sumEven = 0;
        int countOdd = 0;
        System.out.println("Digite 6 números inteiros: ");

        for(int i = 0; i < 6; i++){
            numbers[i] = scanner.nextInt();
        }

        System.out.print("números pares digitados: ");
        for(int num : numbers){
            if(num % 2 == 0){
                System.out.print(num + " ");
                sumEven += num;
            }
        }
        System.out.println();
        System.out.println("Soma dos números pares: " + sumEven);
        System.out.print("Números impares digitados: ");

        for(int num : numbers){
            if(num % 2 != 0){
                System.out.print(num + " ");
                countOdd++;
            }
        }
        System.out.println();
        System.out.println("Quantidade de números ímpares: " + countOdd);
    }

}
