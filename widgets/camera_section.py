import customtkinter as ctk
from PIL import Image
from utils.events import handle_camera_switch
from utils.image_linked_list import ImageNode

def create_camera_section(root):
    frame = ctk.CTkFrame(root, width=450, height=320)
    frame.place(x=20, y=60)

    # CCTV Label
    cctv_label = ctk.CTkLabel(frame, text="CCTV Camera", font=("Arial", 11), text_color='#FDFEFE')
    cctv_label.place(x=10, y=5)

    # On/Off Switch
    camera_switch_var = ctk.StringVar(value="on")
    switch = ctk.CTkSwitch(
        frame, text="",
        command=lambda: handle_camera_switch(camera_switch_var.get()),
        variable=camera_switch_var, onvalue="on", offvalue="off"
    )
    switch.place(x=400, y=20)

    # Image titles and paths
    image_data = [
        ("images/security.jpg", "Front Door"),
        ("images/bed-room1.jpg", "Bedroom 1"),
        ("images/bed-room2.jpg", "Bedroom 2")
    ]

    # Build doubly linked list of images
    head = ImageNode(image_data[0][0], image_data[0][1])
    current = head
    for path, title in image_data[1:]:
        node = ImageNode(path, title)  
        current.next = node
        node.prev = current
        current = node


    # Track current node
    camera_section_state = {"current_node": head}

    # Label that will display the current image title
    title_var = ctk.StringVar(value=head.title)
    image_title_label = ctk.CTkLabel(frame, textvariable=title_var, font=("Arial", 16), text_color='#FDFEFE')
    image_title_label.place(x=10, y=24)

    # Image Label
    img_label = ctk.CTkLabel(frame, text="")
    img_label.place(x=10, y=55)

    # Function to update the image and title
    def update_image():
        node = camera_section_state["current_node"]
        img = ctk.CTkImage(light_image=Image.open(node.image_path), size=(430, 210))
        img_label.configure(image=img)
        img_label.image = img  # type: ignore  # keep reference to avoid GC
        title_var.set(node.title)

    # Navigation buttons
    def show_next():
        if camera_section_state["current_node"].next:
            camera_section_state["current_node"] = camera_section_state["current_node"].next
            update_image()

    def show_prev():
        if camera_section_state["current_node"].prev:
            camera_section_state["current_node"] = camera_section_state["current_node"].prev
            update_image()

    prev_btn = ctk.CTkButton(frame, text="⟨ Prev", command=show_prev, width=70)
    prev_btn.place(x=10, y=270)

    next_btn = ctk.CTkButton(frame, text="Next ⟩", command=show_next, width=70)
    next_btn.place(x=360, y=270)

    # Show initial image
    update_image()