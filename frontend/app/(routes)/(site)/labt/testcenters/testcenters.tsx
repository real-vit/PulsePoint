"use client"


import { cn } from "@/lib/utils"
import TestCenters from "./testc"
import { TestCenterData } from "./testcent"

export const DocShow = () => {
    return(
        <div className={cn("grid mx-auto relative items-center justify-center grid-flow-row gap-6 py-10")}>
            {TestCenters.map((item,index)=>(
            <TestCenterData img={item.img} name={item.name} loc={item.loc} key={index}/>
            ))}
        </div>
    )
}