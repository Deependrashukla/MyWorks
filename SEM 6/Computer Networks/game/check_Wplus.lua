local function check_Wplus(Wplus)
    assert(type(Wplus) == "table")
    for k1, w1 in ipairs(Wplus) do
      assert(type(w1) == "string")
      assert(game.D[w1])
      for i = 1, #game.H do
        assert(game.H[i].word ~= w1)
      end
      for i = 1, #game.W do
        assert(game.W[i] ~= w1)
      end
      for k2, w2 in ipairs(Wplus) do
        if ( k1 ~= k2 ) then 
            assert(w1 ~= w2) 
        end
      end
    end
    return true
  end