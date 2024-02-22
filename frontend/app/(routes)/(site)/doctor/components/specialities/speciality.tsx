"use client"


import { cn } from "@/lib/utils"
import { CircleSpec } from "./special"
import SpecDetails from "./spec"

export const Condi = () => {
    return(
        <div className={cn("grid mx-auto grid-cols-3 relative items-center justify-center grid-flow-row gap-6 md:grid-cols-6 py-10")}>
            {SpecDetails.map((item,index)=>(
            <CircleSpec img={item.img} link={item.link} text={item.text} key={index}/>
            ))}
        </div>
    )
}
