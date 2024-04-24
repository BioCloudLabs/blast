export const Button = ({ onClick, children }) => {
    return (
        <>
            <button 
                className="hover:scale-110 transition-transform ease-out relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-green-400 to-blue-600 group-hover:from-green-400 group-hover:to-blue-600 hover:text-white focus:ring-4 focus:outline-none focus:ring-green-200"
                onClick={onClick}
            >
                <span className="bg-slate-200 relative px-5 py-2.5 transition-opacity duration-150 rounded-md group-hover:bg-opacity-0">
                    {children}
                </span>
            </button>
        </>
    )
}