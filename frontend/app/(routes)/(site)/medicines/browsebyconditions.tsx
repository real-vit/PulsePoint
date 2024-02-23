"use client"

import Conditions from "./try"
import { Circle } from "./conditions"
import { cn } from "@/lib/utils"

export const Cond = () => {
    return(
        <div className={cn("grid mx-auto grid-cols-3 relative items-center justify-center grid-flow-row gap-6 md:grid-cols-6 py-4")}>
            {Conditions.map((item,index)=>(
            <Circle img={item.img} link={item.link} text={item.text} key={index}/>
            ))}
        </div>
    )
}
