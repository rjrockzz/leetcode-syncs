class Solution {
    public double average(int[] salary) {
        if(salary.length <=2) return 0;
        int counter = 0;
        double adder = 0;
        Arrays.sort(salary);
        for(int i = 1; i < salary.length - 1; i++){
            adder = adder + salary[i];
            counter++;
        }
        return adder/counter;
    }
}