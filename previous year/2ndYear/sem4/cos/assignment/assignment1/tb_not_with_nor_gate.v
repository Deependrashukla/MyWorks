`include "not_with_nor_gate.v"

module tb_not_with_nor_gate();

reg b;
wire c;

not_with_nor_gate t1(b,c);

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