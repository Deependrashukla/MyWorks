`include "Demultiplexer_1to4.v"

module demultiplexer_1to4_tb();
reg a,s0,s1;
wire y0,y1,y2,y3;

demultiplexer_1to4 f1(a,s0,s1,y0,y1,y2,y3);

initial begin
    $monitor("a=%b, s0=%b, s1=%b, y0=%b,y1=%b,y2=%b,y3=%b\n", a,s0,s1,y0,y1,y2,y3);
    #2 a=1'b0; s0=1'b0; s1=1'b0;
    #2 a=1'b0; s0=1'b0; s1=1'b1;
    #2 a=1'b0; s0=1'b1; s1=1'b0;
    #2 a=1'b0; s0=1'b1; s1=1'b1;
    #2 a=1'b1; s0=1'b0; s1=1'b0;
    #2 a=1'b1; s0=1'b0; s1=1'b1;
    #2 a=1'b1; s0=1'b1; s1=1'b0;
    #2 a=1'b1; s0=1'b1; s1=1'b1;
end

initial begin
 $dumpfile("out.vcd");
 $dumpvars;
 #20 $finish;
end
endmodule