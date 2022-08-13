import java.util.*;

class Main{

    static int findPeak(int array[], int n)
    {
        // First or last in array is peak
        if(n == 1)
            return 0;
        if(array[0] >= array[1])
            return 0;
        if(array[n - 1] >= array[n - 2])
            return n - 1;

        return 0;
    }


    public static void main(String[] args)
    {
        int myArray = {1,5,58,4,1,0};
        int
    }
}
