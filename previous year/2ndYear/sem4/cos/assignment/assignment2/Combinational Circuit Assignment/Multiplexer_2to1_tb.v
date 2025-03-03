`include "Multiplexer_2to1.v"

module multiplexer_tb();
    reg [1:0] ab;
    reg sel;
    wire c;

multiplexer s1(ab,sel,c);

initial begin
    $monitor("ab=%b, sel=%b, output=%b\n", ab, sel,c);
        #2 ab=2'b00; sel=1'b0;
        #2 ab=2'b00; sel=1'b1;
        #2 ab=2'b01; sel=1'b0;
        #2 ab=2'b01; sel=1'b1;
        #2 ab=2'b10; sel=1'b0;
        #2 ab=2'b10; sel=1'b1;
        #2 ab=2'b11; sel=1'b0;
        #2 ab=2'b11; sel=1'b1;
end

initial begin
    $dumpfile("out.vcd");
    $dumpvars;
    #50 $finish;
end

endmodule