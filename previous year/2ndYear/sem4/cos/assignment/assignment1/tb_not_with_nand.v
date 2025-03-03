`include "not_with_nand.v"

module tb_or_with_nand();

reg b;
wire c;

not_with_nand t1(b,c);

initial begin
    $monitor("input=%b, output=%b\n", b, c);
    #2  b=1'b0;
    #2  b=1'b1;

end

initial begin
 $dumpfile("out.vcd");
 $dumpvars;
 #10 $finish;
end
endmodule