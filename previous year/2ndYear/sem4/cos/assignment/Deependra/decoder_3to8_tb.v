`include "decoder_3to8.v"
module decoder_tb();
reg a,b,c;
wire d0,d1,d2,d3,d4,d5,d6,d7;

decoder s1(a,b,c,d0,d1,d2,d3,d4,d5,d6,d7);

initial begin
    $monitor("a=%b, b=%b, c=%b, d0=%b, d1=%b, d2=%b, d3=%b, d4=%b, d5=%b, d6=%b, d7=%b\n", a,b,c,d0,d1,d2,d3,d4,d5,d6,d7);
    #2 a=1'b0; b=1'b0; c=1'b0;
    #2 a=1'b0; b=1'b0; c=1'b1;
    #2 a=1'b0; b=1'b1; c=1'b0;
    #2 a=1'b0; b=1'b1; c=1'b1;
    #2 a=1'b1; b=1'b0; c=1'b0;
    #2 a=1'b1; b=1'b0; c=1'b1;
    #2 a=1'b1; b=1'b1; c=1'b0;
    #2 a=1'b1; b=1'b1; c=1'b1;
end
endmodule