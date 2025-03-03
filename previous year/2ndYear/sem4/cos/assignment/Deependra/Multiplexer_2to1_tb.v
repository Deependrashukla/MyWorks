`include "Multiplexer_2to1.v"

module multiplexer_tb();
    reg a,b,sel;
    wire c;

multiplexer s1(a,b,sel,c);

initial begin
    $monitor("input=%b, input=%b, input=%b, output=%b\n", a, b, sel,c);
        #2 a=1'b0; b=1'b0; sel=1'b0;
        #2 a=1'b1; b=1'b0; sel=1'b1;
        #2 a=1'b0; b=1'b1; sel=1'b0;
        #2 a=1'b1; b=1'b1; sel=1'b1;
        #2 a=1'b1; b=1'b0; sel=1'b0;
        #2 a=1'b0; b=1'b1; sel=1'b1;
        #2 a=1'b1; b=1'b1; sel=1'b0;
        #2 a=1'b0; b=1'b0; sel=1'b1;
end

initial begin
    $dumpfile("out.vcd");
    $dumpvars;
    #20 $finish;
end
    
endmodule