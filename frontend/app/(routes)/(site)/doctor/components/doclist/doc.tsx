"use client"


import { cn } from "@/lib/utils"

import Doc from "./doctor"
import { DoctorData } from "./doctors"

export const DocShow = () => {
    return(
        <div className={cn("grid mx-auto relative items-center justify-center grid-flow-row gap-6 py-10")}>
            {Doc.map((item,index)=>(
            <DoctorData img={item.img} name={item.name} spl={item.spl} key={index}/>
            ))}
        </div>
    )
}