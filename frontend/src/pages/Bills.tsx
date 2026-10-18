import {LuArrowLeft, LuArrowRight} from "react-icons/lu"



function Bills() {
    return (
        <div className="page-container">
            <div className="months">
                <button><LuArrowLeft/></button>
                <h2> Energy </h2>
                <button><LuArrowRight/></button>
            </div>


        </div>
    )
}

export default Bills;