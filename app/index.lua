-- Hello World for Xteink InkApps (Lua API 2.x, 480 x 800 portrait, 1 bpp).

function on_load(ctx)
  if type(ctx.state) ~= "table" then
    ctx.state = {}
  end
end

function on_draw(_, g)
  g:clear(0)
  g:text(150, 380, "Hello World")
end

function on_input(_, _)
  return false
end

function on_leave() end
