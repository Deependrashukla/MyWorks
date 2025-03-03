`include "tff.v"
module mode_counter(clk, reset, mode, counter);
parameter size=16;
input clk,reset,mode;
output wire [size-1:0]counter;
wire [size-1:0]qb;
wire [size-1:0] t;
wire inv_mode;
wire [size-2:0]adv1, adv2, xr;
assign t[0] =1'd1;

tff tff_inst1(clk,reset,t[0],counter[0],qb[0]);

genvar i;
for (i=1; i<size; i=i+1) begin

if (i==1) begin
  assign adv1[i-1] = counter[i-1] & ~mode;
  assign adv2[i-1] = qb[i-1] & mode;
  assign xr[i-1] = adv1[i-1] ^ adv2[i-1];
end

else begin
    assign adv1[i-1] = counter[i-1] & adv1[i-2];
    assign adv2[i-1] = qb[i-1] & adv2[i-2];
    assign xr[i-1] = adv1[i-1] ^ adv2[i-1];
end
    tff tff_inst2(clk,reset,xr[i-1],counter[i],qb[i]);
end

endmodule