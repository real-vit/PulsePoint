"use client"

import Link from "next/link";

export const HubLink =({
    link,
    dest
}:{
    link:string;
    dest:string;
})=>{
    return(
        <div className="font-bold hover:font-2xl hover:text-white">
            <Link
            href={link}>
                {dest}
            </Link>
        </div>
    )
}