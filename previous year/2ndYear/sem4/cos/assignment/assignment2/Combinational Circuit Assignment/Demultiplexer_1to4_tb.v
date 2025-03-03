`include "Demultiplexer_1to4.v"

module demultiplexer_1to4_tb();
    reg in;
    reg [1:0] sel;
    wire [3:0] out;

demux1_4 f1(in, sel, out);

initial begin
    $monitor("in=%b, sel=%b, out=%b\n", in, sel, out);
    #2 in = 1'b0; sel = 2'b00;
    #2 in = 1'b0; sel = 2'b01;
    #2 in = 1'b0; sel = 2'b10;
    #2 in = 1'b0; sel = 2'b11;
    #2 in = 1'b1; sel = 2'b00;
    #2 in = 1'b1; sel = 2'b01;
    #2 in = 1'b1; sel = 2'b10;
    #2 in = 1'b1; sel = 2'b11;
end
initial begin
    $dumpfile("out.vcd");
    $dumpvars;
    #50 $finish;
end

endmodule
