defmodule MaqarrDemo.Application do
  use Application
  def start(_type, _args) do
    children = [%{id: :http, start: {Task, :start_link, [fn -> serve() end]}}]
    Supervisor.start_link(children, strategy: :one_for_one)
  end
  defp serve do
    port = String.to_integer(System.get_env("PORT", "8000"))
    {:ok, socket} = :gen_tcp.listen(port, [:binary, active: false, reuseaddr: true, ip: {0, 0, 0, 0}])
    IO.puts("maqarr-auto-e2e:elixir:v2 ready")
    accept(socket)
  end
  defp accept(listener) do
    {:ok, socket} = :gen_tcp.accept(listener)
    _ = :gen_tcp.recv(socket, 0, 5000)
    body = Jason.encode!(%{service: "maqarr-auto-e2e:elixir:v2"})
    :gen_tcp.send(socket, "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: #{byte_size(body)}\r\nConnection: close\r\n\r\n#{body}")
    :gen_tcp.close(socket)
    accept(listener)
  end
end
