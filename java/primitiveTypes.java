public class primitiveTypes {
    public static void main(String[] args){
        byte myByteVariable = 127;
        short myShortVariable = 32767;
        int myIntVariable = 50;
        long myLongVariable = 50000 +  10L * (myByteVariable + myShortVariable + myIntVariable);
        System.out.println(myLongVariable);
        // cast as a short
        short shortTotal = (short) (1000 + 10 * 
            (myByteVariable + myIntVariable + myShortVariable));

    }
    
}
