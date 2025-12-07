
# Note 
Your delivery should tie together A3-A5 - And from a users/readers point of view we like to see dedicated references to each of the assignements’ outcomes. Therefore you may want to edit (commit changes to) the README.md in the main path of your project account to point at A3-A5 (A1-A2 is optional), or write a small intro to the Project Reflection and wrap-up that clearly links to each of the sub deliveries in those assignments.


# Your learning experience for the concept you focused on.
- Identify your own level at the beginning of this course and where you ended
- What else do you still need to learn?
- how you might use OpenBIM in the future?

### Line: 
**Identify your own level at the beginning of this course and where you ended:**
At the beginning of the course, I hadn’t even opened VS Code before. I had no practical coding experience, and concepts like data extraction or using IFC commands were completely new to me. Now I can navigate code confidently, pull data from models, and work with a library of IFC commands. I also understand how these tools can be applied in practice, which has significantly increased my technical foundation.
**What else do you still need to learn?**
To get the full benefit of what I’ve learned, I still need to improve my general coding skills. I understand the concepts, but I need more routine, structure, and confidence in writing and debugging code on my own. Strengthening this will make it easier to build more advanced tools and automate larger workflows.
**How you might use OpenBIM in the future:**
The course presentations gave me a lot of inspiration for how OpenBIM can be used, and it was fascinating to see how versatile it is. I plan to use it to streamline my workflow in early design stages, where models change constantly and manual work becomes inefficient. I also see strong potential for applying it in ventilation, heat balance, and daylight calculations, where you often need to handle large amounts of simple geometry and repetitive computations. Automating these processes through OpenBIM will make my work faster, more flexible, and more consistent.

### Dimitris: 
**Identify your own level at the beginning of this course and where you ended:**
At the start of the course, I would describe my level as just a BIM modeller with only basic Python knowledge, I knew the core structures of the language, but nothing advanced. By the end, I was able to extract data from IFC models, work confidently with ifcopenshell and understand code directly related to OpenBIM.

**What else do you still need to learn?**
Sky is the limit of what there is still left to learn. We only scratched the surface of what coding can do to complement BIM models. I still want to strengthen my programming skills in general, but also dive deeper into the geometric side of ifcopenshell. Proper bounding-box handling and geometric queries seem essential, especially for complex models where geometry becomes the fallback to map or interpret elements correctly.

**How you might use OpenBIM in the future:**
Digital Twins are  the direction I would like to explore. I want to understand how we can take OpenBIM models and layer additional information onto them to create a “living” representation of a building throughout its lifecycle. 

### Nikoletta:
**Identify your own level at the beginning of this course and where you ended:**
At the start of the course, I had no experience with programming at all and I didn’t know how code could interact with BIM models. Everything felt completely new and a bit confusing. Now, I can write scripts, extract data from IFC models, and understand how OpenBIM tools work in practice. I feel more confident exploring code, trying commands, and thinking about how these tools can help in real projects.

**What else do you still need to learn?**
I still need a lot of practice to feel fully confident coding on my own. I want to get better at handling more complex data and automating tasks efficiently. I would also like to learn ifcopenshell more deeply, so I can use all its features and work faster with IFC models. Improving my Python skills will help me make more advanced scripts and handle bigger challenges in BIM.

**How you might use OpenBIM in the future:**
I’m really interested in the indoor environment of a building, like how air quality, lighting, and temperature affect comfort.In the future, I would like to explore how OpenBIM can help me work with these aspects in a general way, analyzing and optimizing indoor conditions for comfort and efficiency. This would help design houses or apartments that are more comfortable and energy-efficient. One idea I find exciting is creating small evaluation tools that compare different design options early in the process, so you can quickly see which layout provides better comfort or energy performance without doing everything manually.

# Your process of developing the tutorial
- Did the process of the course enable you to answer or define questions that you might need later for thesis?
- Would you have preferred to have been given less choice in the use cases?
- Was the number of tools for the course ok - should we have more or less? - if so which ones would you leave out?

### Line:
**Did the process of the course enable you to answer or define questions you might need later for your thesis?**
        Yes. The process helped me understand how to frame the right questions and identify what I need to investigate further, especially regarding data handling, automation, and how BIM tools can support early-stage design.
**Would you have preferred less choice in the use cases?**
        The large amount of freedom was a bit daunting at first, especially without supervision, and it made it easy to accidentally choose something too difficult. But the openness was also very valuable, because it allowed for a wide range of tools and approaches without a fixed standard of what “finished” had to look like. I would have liked some guidance or feedback early on to help evaluate ideas and their feasibility.
**Was the number of tools for the course okay? Should we have more or less? If so, which ones?**
        I dont understand the question.

### Dimitris: 
**Did the process of the course enable you to answer or define questions you might need later for your thesis?**
Yes. The course helped a lot, especially because all the material was available from the beginning. I also really enjoyed working with GitHub. It was my first time using it, and I will absolutely keep using it in future projects.
If anything, I would have appreciated a slightly more structured introduction in the early weeks, perhaps a set of small, guided exercises on basic data extraction before diving into self-directed exploration of the ifcopenshell library. That would have helped build confidence faster.

**Would you have preferred less choice in the use cases?**
I think the level of freedom in choosing use cases was fine. It allowed each of us to explore something closer to our own skills and interests. Even though our initial use-case turned out to be quite ambitious, it was easy to switch, refine, or scale it according to what was realistic within our time and coding abilities.

**Was the number of tools for the course okay? Should we have more or less? If so, which ones?**
I think the number of tools for the purposes that this course is trying to achieve was sufficient.

### Nikoletta:
**Did the process of the course enable you to answer or define questions you might need later for your thesis?**
Yes, the course definitely helped me understand what kind of questions I should ask when working with BIM data and coding. It made me think more clearly about how to structure a problem and what information I actually need to look at. I feel that this will be useful later for my thesis, especially if it involves analysis, automation, or using IFC models in any way.

**Would you have preferred less choice in the use cases?**
The freedom we had was both good and difficult at the same time. In the beginning, it was challenging because we didn’t always know what to do or how to move forward, especially since we were still getting used to the tools. We often got stuck or reached dead ends when trying to choose a direction for our project. But in the end, this process helped us learn a lot. It pushed us to explore, search for solutions, and try different ideas until we found something that actually worked. Even though it was sometimes frustrating, it was also very productive for our learning.

**Was the number of tools for the course okay? Should we have more or less? If so, which ones?**
I think the number of tools was fine. It felt balanced, not too many and not too few. I don’t think anything specific needs to be removed. What would help even more is having a bit more guidance or examples at the beginning, just so we can understand how to use the tools more confidently before experimenting on our own.



# (As a group) summary of the feedback you received on your tutorial

- did the tool address the use case you identified?
- What stage does the tool you created work in Advanced Building Design? ( Stage A, B, C and/ or D).

# Feedback

## Presentation

### Why did it need the MEP file?
It was a leftover from the early stages of tool development. The original idea was to use the MEP model to check duct outlet sizing and outlet counts, which would have been ideal. However, as we moved deeper into the ventilation calculations, the scope became more extensive than expected. Because of that, the tool still has a lot of potential for further development and additional features.

### Could you keep the data in VS (the program) for later processing and analysis?
Yes. You would simply need to recode how the information is stored. Once adjusted, the tool could easily be expanded, or the extracted data could be reused for further analysis.

## Group feedback
- Good job building the tool. A lot of the required information can be difficult to extract or locate.
- Consider using the given occupancy data if available.
- It would be useful if the program accessed the model and informed the user whether sufficient information is available, and what data is missing.
- BCF files could be used to show errors clearly, making it easier to identify what exactly is wrong.
- Make it clear that the MEP file was originally intended for use in the code but is not actually incorporated. The current version of the tool only needs the ARCH file to function in theory.
- Using chair count for occupancy makes sense, since ventilation is typically dimensioned based on a fully occupied space.




# (Individual) Your future for Advanced use of OpenBIM
- are you likely to use OpenBIM tools in your thesis?
- are you likely to use OpenBIM tools in your professsional life in the next 10 years?

## Line:
**Are you likely to use OpenBIM tools in your thesis?**
I am very likely to use OpenBIM tools in my thesis. I find them extremely versatile and adaptable once you understand how they work. They are especially valuable for checking the model's level of completion, ensuring consistency in data, and streamlining long or complex processes that would otherwise be time-consuming to handle manually.
**Are you likely to use OpenBIM tools in your professional life in the next 10 years?**
Yes. I plan to use OpenBIM regularly, as it streamlines workflows, automates repetitive tasks, and supports design and quality control. In roles like project manager or graphic communicator, these tools will be essential as the industry moves toward open, transparent data.

## Dimitris: 
**Are you likely to use OpenBIM tools in your thesis?**
Probably yes. If my thesis involves any form of smart building research, Digital Twins or data-driven design, I expect that OpenBIM tools will play a role in my workflow.
**Are you likely to use OpenBIM tools in your professional life in the next 10 years?**
Also yes, as discussed during the course, these tools are expected to gain  momentum and gradually become an integrated part of architectural, MEP, and structural design processes. Learning them now feels like a strong long-term investment.

## Nikoletta: 
**Are you likely to use OpenBIM tools in your thesis?**
Yes, I think there is a big chance that I will use OpenBIM tools in my thesis. The course showed me how useful IFC data can be for analyzing buildings and testing ideas without doing everything manually. If my thesis ends up focusing on topics like indoor environment, energy performance, or any kind of design evaluation, then OpenBIM tools could help me organize data, run checks, and automate parts of the process.
**Are you likely to use OpenBIM tools in your professional life in the next 10 years?**
Yes, I believe so. OpenBIM tools are becoming more important in the industry, and the ability to work with data directly from IFC models will be useful in many areas. Whether it’s for design checks, automation, coordination, or evaluating building conditions, I can see OpenBIM making everyday workflows much faster and more reliable. Even if the exact tasks change in the future, having these skills will definitely be an advantage.



# (Individual) Wrap up
- conclude the journey through A1-A5

### Line:
The assignments were fairly straightforward. As mentioned earlier, the freedom was enjoyable and allowed for a wide variety of applications, though more guidance would have been helpful. In the first part of the course, the difficulty level allowed us to work on our own projects, learn the basics individually, and deliver the best working tool.

In the later part of the course, it was more challenging to code and integrate our different parts, especially since we often worked individually and had slightly different expectations for what the tools should achieve. It was also difficult to fully develop the tools, even with the provided library of commands, without prior coding experience. I relied on my more experienced teammates and ChatGPT for some of the more complex coding, but the experience was still valuable, and I learned a lot from understanding and editing the scripts. Overall, the course went well, and it was rewarding to create tools that could actually be used and further developed in the future.

It was also very valuable that all projects were presented, allowing us to ask questions and learn from each other. The tutorials were particularly helpful, ensuring that we understood our tools and enabling everyone to quickly grasp their function and then ask questions to their applications, limitations, and potential for further development.

My main criticisms of the course are the room, which was unsuitable for lectures and presentations, and the assignment descriptions. While we received a lot of information, it was sometimes difficult to clearly identify the exact deliverables.


### Dimitris:
The assignments were overall pretty straightforward, although the learning curve was quite steep if you were unfamiliar with coding. In general, I really enjoyed the process. A1 and A2 were especially informative, starting with an initial case in A1 that helped set the mindset for what was coming later in the course.

In A2, updating or selecting a more complex claim and developing a business diagram was also very interesting, as this was the first time we really started thinking about tool creation and software development in a more structured way. At that stage, we were still unsure how well our claim would match our coding skills, and this required much more research into the ifcopenshell library—understanding what information we could extract, how different models behave, and what was realistically achievable.

A3 and A4 demanded continuous research to become familiar with the tools and the library, followed by a lot of testing to see whether we could approach our claim in a way that would produce accurate results and useful output for users. This was a very informative phase, as it clearly showed how much adaptation is needed during tool development. We constantly had to adjust our approach to stay within our current technical skills while still aiming to produce something meaningful.

In general, the journey through A1–A5 helped me better understand OpenBIM and ifcopenshell and also how digital tools are developed through iteration, testing and refinement. It was a clear shift from simply using BIM tools to actively thinking about how they can be extended and customized through coding.

### Nikoletta:

Looking back at the whole journey from A1 to A5, I think it was a very interesting and meaningful process. The structure of the assignments helped us learn step by step, and even though we faced several difficulties along the way, we managed to overcome them. Still, by the end, everything came together in a way that really made us learn.

A1 was a simple and smooth introduction. It didn’t take much time, but it was a good starting point and helped us understand the basic idea of what was coming next.

A2 was a bit more challenging. We had to develop a business diagram for the next parts of the project, and the difficult part was not the time needed but the uncertainty. Since we didn’t know yet what would work later or what direction our project would take, it was hard to define something solid. It took us some time to build a framework that could give us enough flexibility for the following steps.

A3 and A4 were definitely the most demanding sections. We spent a lot of time on trial and error. Even though we had a main plan, we often ran into problems, sometimes things didn’t work as expected, sometimes the window heights were off, and we frequently changed ideas. We also had issues with the bounding box, so we kept testing different approaches. In the end, after many attempts, we managed to create something we were proud of, but it really required patience and effort.

Overall, the whole process taught us a lot. Even though some parts were quite tough and the difficulty could have been more evenly spread from A1 to A5. We learned new tools and new ways of thinking.
