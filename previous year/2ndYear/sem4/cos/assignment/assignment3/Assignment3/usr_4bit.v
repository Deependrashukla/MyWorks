module univ_shift_reg (
    input wire clk, rst,
    input wire [1:0] ctrl,
    input wire [3:0] d,
    output wire [3:0] q
);

reg [3:0] r_current, r_next;
always @(posedge clk or posedge rst) begin
    if (rst) 
        r_current <= 4'b0000;
    else
        r_current <= r_next;
end
always @* begin
    case (ctrl)
        2'b00: r_next = r_current;
        2'b01: r_next = {r_current[2:0], d[0]};
        2'b10: r_next = {d[3], r_current[3:1]};
        default: r_next = d; 
    endcase
end
assign q = r_current;
endmodule
