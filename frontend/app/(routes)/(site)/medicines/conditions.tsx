"use client";


import Image from "next/image"
import Link from "next/link";

 export const Circle=({
    img,link,text}:{
        img: string;
        link: string;
        text:  string;
    }
 )=>{
    return(
        <div className="z-20 border-black-5">
            <div className="flex w-32 h-32 rounded-full hover:opacity-85 text-center">
            <Link href={link} target="_blank">
                <Image  className="align-self-center"
                src= {img}
                width={200}
                height={200}
                alt={text}
                />
                </Link>
          </div>
          <br/>
          <p className="self-between text-center font-bold">{text}</p>
        </div>
         
     )
 }