"use client"

import Link from "next/link"
import LinkData from "./links"
import { NavLink } from "./navlinks"
import { Button, buttonVariants } from "@/components/ui/button"
import { Sparkle } from "lucide-react"
import { MobileSidebar } from "../hubnav/mobilehubnav"


export const Navbar=()=>{
    return(
        <div className="w-full z-50 flex justify-between items-center py-2 px-4
        border-b border-primary/10 bg-secondary h-16 relative bg-gradient-to-r from-green-500 via-teal-300 to-sky-600 text-white-border-0 backdrop-blur-lg">
            <div className="flex items-center">
            <Link href="/">
                <h1 className={
                    "md:block text-xl md:text-3xl font-bold text-primary text-center md:text-justify"}>
                    PulsePoint
                </h1>
            </Link>
                </div> 
                <div className="flex items-center gap-x-3">
            <div className="md:flex hidden space-x-4 gap-x-5 pr-4 items-center">
              {LinkData.map((item, index) => (
                <NavLink link={item.link} dest={item.dest} key={index} />
              ))}
            </div>
            <Link className={buttonVariants({ variant: "outline" })} href="/medicines">Login/Signup</Link>
            </div>

            
        </div>
    )
}