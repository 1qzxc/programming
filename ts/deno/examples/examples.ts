let name1: string;
name1 = 'luigi'

console.log(name1);


const decoder = new TextDecoder('utf-8');
const data1 = await Deno.readFile('readme.txt');
console.log(decoder.decode(data1));

const encoder = new TextEncoder();
const text = encoder.encode('somestring2');

await Deno.writeFile('readme.txt', text);

const response = await fetch('https://swapi.dev/api/films');
const data2 = await response.json();

console.log(data2);


import { v4 } from "https://deno.land/std/uuid/mod.ts"

const uid = v4.generate();
console.log(uid);

const data3 = JSON.parse(Deno.readTextFileSync('./example.json'));
console.log(data3)

import { serve } from "https://deno.land/std@0.128.0/http/server.ts";
import { serveDir } from "https://deno.land/std@0.128.0/http/file_server.ts";

const server = 'null'; 
serve((req) => {
    const pathname = new URL(req.url).pathname;
    if (pathname.startsWith("/static")) {
             return serveDir(req, {
               fsRoot: "path/to/static/files/dir",
             });
    }
    return new Response("request url :" + req.url);
});
    
console.log("http://localhost:8000/");
