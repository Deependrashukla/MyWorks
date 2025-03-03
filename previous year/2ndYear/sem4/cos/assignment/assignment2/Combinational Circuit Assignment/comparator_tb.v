`include "comparator.v"

module tb_3bit_comparator;
    reg [2:0] a, b;
    wire gt, eq, lt;

bit3_comparator f1(a, b, gt, eq, lt);

initial begin
    $monitor("a=%b, b=%b, out=%b%b%b", a,b, gt, eq, lt);
    #5 a = 3'b111; b = 3'b000;
    #5 a = 3'b000; b = 3'b111;
    #5 a = 3'b111; b = 3'b111;
    #5 a = 3'b100; b = 3'b000;
    #5 a = 3'b110; b = 3'b100;
    #5 a = 3'b011; b = 3'b111;
    #5 a = 3'b000; b = 3'b001;
end

initial begin
    $dumpfile("outdslkjh.vcd");
    $dumpvars;
    #100 $finish;
end

endmodule
