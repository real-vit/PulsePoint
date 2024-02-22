"use client";


import Image from "next/image"
import Link from "next/link";

 export const CircleSpec=({
    img,link,text}:{
        img: string;
        link: string;
        text:  string;
    }
 )=>{
    return(
        <div className="z-20 border-black-5">
            <div className="flex  w-32 h-32 rounded-full py-8 px-2 text-center">
            <Link href={link} target="_blank">
                <Image 
                src= {img}
                width={200}
                height={200}
                alt={text}
                />
                </Link>
          </div>
          <br/>
          <p className="self-between">{text}</p>
        </div>
         
     )
 }