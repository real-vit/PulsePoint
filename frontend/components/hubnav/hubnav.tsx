"use client";

import { ClipboardPlus, FolderCheck, Home, Pill, Plus, Settings, Stethoscope } from "lucide-react";
import { usePathname, useRouter } from "next/navigation";

import { cn } from "@/lib/utils";




export const Sidebar = () => {

  const router = useRouter();
  const pathname = usePathname();

  const routes = [
    {
      icon: Home,
      href: '/hom',
      label: "Home",
      pro: false,
    },
    {
      icon: Pill,
      href: '/medicines',
      label: "Medicines",
      pro: true,
    },
    {
      icon: Stethoscope,
      href: '/doctor',
      label: "My Doctor",
      pro: false,
    },

    {
      icon: FolderCheck,
      href: '/labt',
      label: "My Reports",
      pro: false,
    },
    {
      icon: ClipboardPlus ,
      href: '/health',
      label:"My Health",
      pro: false,
    },
  ];


  const onNavigate= (url: string, pro: boolean)=>{
    return router.push(url)
  }
  return (
    <div className="space-y-4 flex flex-col h-full text-primary bg-secondary">
      <div className="p-3 flex-1 flex justify-center">
        <div className="space-y-2">
          {routes.map((route) => (
            <div
              onClick={()=>onNavigate(route.href, route.pro)}
              key={route.href}
              className={cn(
                "text-muted-foreground text-xs group flex p-3 w-full justify-start font-medium cursor-pointer hover:text-primary hover:bg-primary/10 rounded-lg transition",
                pathname === route.href && "bg-primary/10 text-primary",
              )}
            >
              <div className="flex flex-col gap-y-2 items-center flex-1">
                <route.icon className="h-5 w-5" />
                {route.label}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};