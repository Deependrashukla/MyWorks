`include "encoder_8to3.v"

module encode_tb;
reg a7,a6,a5,a4,a3,a2,a1,a0;
wire y2,y1,y0;

encoder s1(a7,a6,a5,a4,a3,a2,a1,a0,y2,y1,y0);

initial begin
    $monitor("a7=%b, a6=%b, a5=%b, a4=%b, a3=%b, a2=%b, a1=%b, a0=%b, y2=%b, y1=%b, y0=%b\n", a7, a6, a5, a4, a3, a2, a1, a0, y2, y1, y0);
    
    #2 a7 = 1'b0; a6 = 1'b0; a5 = 1'b0; a4 = 1'b0; a3 = 1'b0; a2 = 1'b0; a1 = 1'b0; a0 = 1'b1;
    #2 a7 = 1'b0; a6 = 1'b0; a5 = 1'b0; a4 = 1'b0; a3 = 1'b0; a2 = 1'b0; a1 = 1'b1; a0 = 1'b0;
    #2 a7 = 1'b0; a6 = 1'b0; a5 = 1'b0; a4 = 1'b0; a3 = 1'b0; a2 = 1'b1; a1 = 1'b0; a0 = 1'b0;
    #2 a7 = 1'b0; a6 = 1'b0; a5 = 1'b0; a4 = 1'b0; a3 = 1'b1; a2 = 1'b0; a1 = 1'b0; a0 = 1'b0;
    #2 a7 = 1'b0; a6 = 1'b0; a5 = 1'b0; a4 = 1'b1; a3 = 1'b0; a2 = 1'b0; a1 = 1'b0; a0 = 1'b0;
    #2 a7 = 1'b0; a6 = 1'b0; a5 = 1'b1; a4 = 1'b0; a3 = 1'b0; a2 = 1'b0; a1 = 1'b0; a0 = 1'b0;
    #2 a7 = 1'b0; a6 = 1'b1; a5 = 1'b0; a4 = 1'b0; a3 = 1'b0; a2 = 1'b0; a1 = 1'b0; a0 = 1'b0;
    #2 a7 = 1'b1; a6 = 1'b0; a5 = 1'b0; a4 = 1'b0; a3 = 1'b0; a2 = 1'b0; a1 = 1'b0; a0 = 1'b0;
end

initial begin
 $dumpfile("out.vcd");
 $dumpvars;
 #100 $finish;
end
endmodule