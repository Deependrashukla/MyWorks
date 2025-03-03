`include "usr_4bit.v"
`timescale 1ns / 1ps

module univ_shift_reg_tb;
    reg clk;
    reg rst;
    reg [1:0] ctrl;
    reg [3:0] d;
    wire [3:0] q;

    univ_shift_reg inst1 (.clk(clk), .rst(rst), .ctrl(ctrl), .d(d), .q(q));

    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    initial begin
        rst = 0;

        #10; ctrl = 2'b11; d = 4'b1010;
        #10; ctrl = 2'b01;
        #10; ctrl = 2'b10;
        #10; ctrl = 2'b00;

        #10; ctrl = 2'b11;d = 4'b1010;
        #10; ctrl = 2'b01;
        #10; ctrl = 2'b01;
        #10; ctrl = 2'b01;
                
        #10; ctrl = 2'b11;d = 4'b1010;
        #10; ctrl = 2'b10;
        #10; ctrl = 2'b10;
        #10; ctrl = 2'b10;
    end
always @(negedge clk ) begin
    $monitor("ctrl = %b, input = %b, output = %b",  ctrl, d, q);
end
initial begin
    $dumpfile("out.vcd");
    $dumpvars;
    #130 $finish;
end

endmodule
