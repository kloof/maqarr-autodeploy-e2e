require 'webrick'
$stdout.sync = true
server=WEBrick::HTTPServer.new(Port: Integer(ENV.fetch('PORT','8000')),BindAddress:'0.0.0.0',Logger: WEBrick::Log.new($stdout),AccessLog:[])
server.mount_proc('/') { |_request,response| response['Content-Type']='text/html';response.body='<h1>maqarr-auto-e2e:ruby:v1</h1>' }
trap('TERM') { server.shutdown }
puts 'maqarr-auto-e2e:ruby:v1 ready'
server.start
