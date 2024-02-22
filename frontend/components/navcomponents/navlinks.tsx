"use client"

import Link from "next/link";

export const NavLink =({
    link,
    dest
}:{
    link:string;
    dest:string;
})=>{
    return(
        <div className="font-bold">
            <Link
            href={link}>
                {dest}
            </Link>
        </div>
    )
}