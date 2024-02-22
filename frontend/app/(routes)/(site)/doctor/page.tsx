import { Hub } from "@/components/hubnav/hub";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";

export default function Home () {
    return(
        <div className="mx-auto items-center">
            <Hub/>
            <br />
            <br />
            <Input className="w-1/2 self-center px-5" type="text" placeholder="Search for Doctors or Specialities..."/>
            <br />
            <Separator/>

            <div className="py-3">
                <p>Choose from the best doctors across the city...</p>
            </div>
        </div>
    )
}