module
wire q0, q1,q2,q3;
reg [0:3]A;
four_bit_reg memory(A,clk,q0,q1,q2,q3);
initial begin
    $monitor("%b,%b,%b,%b,%b", A, q0,q1,q2,q3);
    clk = 1'b1;
    A = 4'b1101;
    #10

    #10
    clk = 1'b0;
    A = 4'b1001;
    clk = 1'b0;
end
endmodule