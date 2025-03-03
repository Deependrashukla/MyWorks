`include "encoder_8to3.v"

module encode_tb;
    reg [7:0] in;
    wire [2:0] out;

encoder8to3 s1(in, out);

initial begin
    $monitor("in=%b, out=%b", in, out);
    #2 in = 8'b00000001;
    #2 in = 8'b00000010;
    #2 in = 8'b00000100;
    #2 in = 8'b00001000;
    #2 in = 8'b00010000;
    #2 in = 8'b00100000;
    #2 in = 8'b01000000;
    #2 in = 8'b10000000;
    end

initial begin
    $dumpfile("out.vcd");
    $dumpvars;
    #50 $finish;
end
endmodule
