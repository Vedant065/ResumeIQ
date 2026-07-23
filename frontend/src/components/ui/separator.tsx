import * as SeparatorPrimitive from "@radix-ui/react-separator";

import { cn } from "@/lib/utils";

function Separator({
  className,
  orientation = "horizontal",
}: {
  className?: string;
  orientation?: "horizontal" | "vertical";
}) {
  return (
    <div
      className={cn(
        orientation === "horizontal"
          ? "h-px w-full bg-gray-200"
          : "h-full w-px bg-gray-200",
        className
      )}
    />
  );
}

export { Separator };
