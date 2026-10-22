use std::{io::{Read,Write},net::TcpListener};
fn main(){
    let port=std::env::var("PORT").unwrap_or_else(|_|"8000".into());
    let listener=TcpListener::bind(format!("0.0.0.0:{port}")).expect("listen");
    println!("maqarr-auto-e2e:rust:ci-pass ready");
    for mut stream in listener.incoming().flatten(){
        let _=stream.set_read_timeout(Some(std::time::Duration::from_secs(5)));
        let mut buffer=[0;8192];let size=stream.read(&mut buffer).unwrap_or(0);
        let mut headers=[httparse::EMPTY_HEADER;32];
        let mut request=httparse::Request::new(&mut headers);
        if request.parse(&buffer[..size]).is_ok(){
            let body="<h1>maqarr-auto-e2e:rust:ci-pass</h1>";
            let _=write!(stream,"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",body.len(),body);
        }
    }
}
