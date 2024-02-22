import { Sidebar } from "@/components/hubnav/hubnav";
import { MobileSidebar } from "@/components/hubnav/mobilehubnav";
import { cn } from "@/lib/utils";
import { Scroll } from "./trial";
import { Hub } from "@/components/hubnav/hub";
import DoingToday from "./try";
import { Separator } from "@/components/ui/separator";
import { Button } from "@/components/ui/button";
import { Boxes } from "lucide-react";


export default function Home () {
    return(
        <div className="mx-auto items-center">
            <Hub/>
            <br />
            <br />
            <div className="mx-auto items-center">
                <h3 className="font-semibold px-5">How can we help you today?</h3>
                 <Scroll/>
            </div>
            <br />

            <br />
            <div className="mx-auto items-center">
                <h3 className="font-semibold px-5">Buy Again from your previous order</h3>
                 {/* Add link with backend */}
                 <Button variant={"outline"}>Go to My Orders.... <Boxes/></Button>
            </div>

            <br />
            <div className="mx-auto items-center">
                <h3 className="font-semibold px-5">Browse by Health Condition...</h3>
                 <Scroll/>
            </div>
            <br />

        </div>
    )
}